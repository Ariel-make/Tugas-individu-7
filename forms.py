from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import (AnyOf, DataRequired, Email, Length,
                                NumberRange, Optional, Regexp, ValidationError)

from data import BOBOT, matakuliah, semester_berjalan


class KontakForm(FlaskForm):
    nama = StringField("Nama", validators=[
        DataRequired(message="Nama wajib diisi."),
        Length(min=3, max=50, message="Nama harus 3–50 karakter."),
    ])
    email = StringField("Email", validators=[
        DataRequired(message="Email wajib diisi."),
        Email(message="Format email tidak valid."),
    ])
    telepon = StringField("Telepon (opsional)", validators=[
        Optional(),
        Regexp(r"^(08|\+62)\d{8,12}$", message="Gunakan format 08xxxxxxxxxx atau +62xxxxxxxxxx."),
    ])
    pesan = TextAreaField("Pesan", validators=[
        DataRequired(message="Pesan wajib diisi."),
        Length(min=10, max=500, message="Pesan harus 10–500 karakter."),
    ])


class MatakuliahForm(FlaskForm):
    kode = StringField("Kode (8 digit angka)", validators=[
        DataRequired(message="Kode wajib diisi."),
        Regexp(r"^\d{8}$", message="Kode harus tepat 8 digit angka."),
    ])
    nama = StringField("Nama matakuliah", validators=[
        DataRequired(message="Nama matakuliah wajib diisi."),
        Length(min=3, max=80, message="Nama harus 3–80 karakter."),
    ])
    smt = IntegerField("Semester (1-8)", validators=[
        DataRequired(message="Semester wajib diisi (angka)."),
        NumberRange(min=1, max=8, message="Semester harus 1–8."),
    ])
    sks = IntegerField("SKS (1-6)", validators=[
        DataRequired(message="SKS wajib diisi (angka)."),
        NumberRange(min=1, max=6, message="SKS harus 1–6."),
    ])
    nilai = SelectField("Nilai",
                        choices=[("", "Pilih...")] + [(n, n) for n in BOBOT],
                        validators=[
                            DataRequired(message="Nilai wajib dipilih."),
                            AnyOf(list(BOBOT), message="Nilai tidak valid."),
                        ])

    # Validator custom: WTForms otomatis memanggil validate_<nama_field>
    def validate_kode(self, field):
        sudah_ada = {mk["kode"] for mk in matakuliah + semester_berjalan}
        if field.data in sudah_ada:
            raise ValidationError("Kode matakuliah ini sudah terdaftar.")