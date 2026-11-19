from flask import Flask, render_template

from data import (BOBOT, PROFIL, hitung_ipk, hitung_total_sks, matakuliah,
                  nilai_dengan_nk, semester_berjalan)

app = Flask(__name__)


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
                           dist=dist, sks_smt=sks_smt, max_sks=max(x["sks"] for x in sks_smt))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
