import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf.csrf import CSRFError, CSRFProtect

from data import (BOBOT, PROFIL, hitung_ipk, hitung_total_sks, matakuliah,
                  nilai_dengan_nk, pesan_masuk, semester_berjalan)
from forms import KontakForm, MatakuliahForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "ganti-dengan-kunci-rahasia-kamu")
csrf = CSRFProtect(app)  # CSRF aktif otomatis untuk semua request POST


@app.context_processor
def inject_global():
    """Variabel yang otomatis tersedia di SEMUA template (navbar, footer, dll)."""
    return {"profil": PROFIL}


def ringkasan():
    return {
        "ipk": f"{hitung_ipk(matakuliah):.2f}",
        "total_sks": hitung_total_sks(matakuliah) + hitung_total_sks(semester_berjalan),
        "jumlah_mk": len(matakuliah) + len(semester_berjalan),
    }


@app.route("/")
def index():
    return render_template("index.html", data_js={"matakuliah": matakuliah, "semesterBerjalan": semester_berjalan})


# ---------- FORM 1: kontak (publik) ----------
@app.route("/kontak", methods=["GET", "POST"])
def kontak():
    form = KontakForm()
    if form.validate_on_submit():
        pesan_masuk.append({
            "nama": form.nama.data,
            "email": form.email.data,
            "telepon": form.telepon.data or "-",
            "pesan": form.pesan.data,
            "waktu": datetime.now().strftime("%d %b %Y %H:%M"),
        })
        flash("Terima kasih! Pesanmu sudah terkirim.", "success")
        return redirect(url_for("kontak"))  # PRG: redirect setelah POST berhasil
    return render_template("kontak.html", form=form)


# ---------- FORM 2: tambah matakuliah (admin) ----------
@app.route("/admin/matakuliah/tambah", methods=["GET", "POST"])
def tambah_matakuliah():
    form = MatakuliahForm()
    if form.validate_on_submit():
        matakuliah.append({
            "kode": form.kode.data,
            "nama": form.nama.data.strip(),
            "smt": form.smt.data,
            "sks": form.sks.data,
            "nilai": form.nilai.data,
        })
        flash(f"Matakuliah “{form.nama.data.strip()}” berhasil ditambahkan.", "success")
        return redirect(url_for("admin_dashboard"))  # PRG
    return render_template("admin/tambah_matakuliah.html", form=form)


@app.route("/admin")
def admin_dashboard():
    # distribusi nilai untuk grafik batang (dihitung di Python, digambar dengan CSS)
    dist = []
    for n in BOBOT:
        jumlah = sum(1 for mk in matakuliah if mk["nilai"] == n)
        if jumlah:
            dist.append({"nilai": n, "jumlah": jumlah, "persen": round(jumlah / len(matakuliah) * 100)})
    sks_smt = [{"smt": s, "sks": hitung_total_sks([m for m in matakuliah + semester_berjalan if m["smt"] == s])}
               for s in (1, 2, 3)]
    return render_template("admin/dashboard.html", stats=ringkasan(), daftar=nilai_dengan_nk(matakuliah),
                           dist=dist, sks_smt=sks_smt, max_sks=max(x["sks"] for x in sks_smt),
                           pesan_masuk=pesan_masuk)


@app.errorhandler(CSRFError)
def csrf_error(e):
    return render_template("400.html", alasan=e.description), 400


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
