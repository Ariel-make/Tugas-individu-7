"""Data & fungsi hitung (pindahan dari array JavaScript Tugas Individu 2)."""

PROFIL = {
    "nama": "Ariel Alvian Yusuf",
    "nbi": "1482500001",
    "role": "Mahasiswa · Sistem Teknologi Informasi",
    "prodi": "Sistem Teknologi Informasi",
    "kampus": "Untag Surabaya",
    "telp": "+62 823-3758-7860",
    "email": "arielalfianyusuf@gmail.com",
    "lokasi": "Surabaya, Indonesia",
    "tentang": [
        "Perkenalkan, saya Ariel Alvian Yusuf, lahir pada 26 November 2006 dan saat ini berusia 19 tahun. "
        "Saya sedang menempuh pendidikan S1 Program Studi Sistem Teknologi Informasi di Universitas 17 Agustus 1945 Surabaya.",
        "Saya tertarik dengan dunia teknologi, khususnya pengembangan website dan keamanan siber.",
    ],
    "hobi": [
        "Ngotak-ngatik OS seperti Ubuntu, Kali Linux, dan Parrot Security OS",
        "Belajar hal-hal baru",
        "Bermain game",
    ],
    "pendidikan": [
        "SMK Labschool Unesa 1 Surabaya",
        "S1 Sistem Teknologi Informasi, Universitas 17 Agustus 1945 Surabaya (sedang berjalan)",
    ],
    "keahlian": ["HTML & CSS", "Basic Programming", "Editor Video", "Videografer"],
}

matakuliah = [
    {"kode": "14823153", "nama": "Teknologi Informasi dan Aplikasi Bisnis Berkembang", "smt": 2, "sks": 3, "nilai": "B"},
    {"kode": "14823372", "nama": "Statistika dan Probabilitas", "smt": 2, "sks": 2, "nilai": "A"},
    {"kode": "14823313", "nama": "Sistem Basis Data", "smt": 2, "sks": 3, "nilai": "AB"},
    {"kode": "14823274", "nama": "Pemrograman Berorientasi Objek", "smt": 2, "sks": 4, "nilai": "AB"},
    {"kode": "14823393", "nama": "Interaksi Manusia Komputer", "smt": 2, "sks": 3, "nilai": "B"},
    {"kode": "14823333", "nama": "Algoritma dan Struktur Data", "smt": 2, "sks": 3, "nilai": "AB"},
    {"kode": "14823192", "nama": "Arsitektur dan Organisasi Komputer", "smt": 2, "sks": 2, "nilai": "AB"},
    {"kode": "14823532", "nama": "Bahasa Inggris", "smt": 1, "sks": 2, "nilai": "AB"},
    {"kode": "14823103", "nama": "Konsep dan Fondasi Sistem Informasi", "smt": 1, "sks": 3, "nilai": "AB"},
    {"kode": "14823202", "nama": "Sistem Operasi", "smt": 1, "sks": 2, "nilai": "AB"},
    {"kode": "14823342", "nama": "Aljabar Linier", "smt": 1, "sks": 2, "nilai": "A"},
    {"kode": "14823362", "nama": "Kalkulus", "smt": 1, "sks": 2, "nilai": "B"},
    {"kode": "14823352", "nama": "Matematika Diskrit", "smt": 1, "sks": 2, "nilai": "B"},
    {"kode": "14823323", "nama": "Dasar Pemrograman", "smt": 1, "sks": 3, "nilai": "B"},
    {"kode": "14823012", "nama": "Etika Pengembangan Teknologi Siber", "smt": 1, "sks": 2, "nilai": "B"},
]

semester_berjalan = [
    {"kode": "14823213", "nama": "Desain Jaringan Komputer dan Komunikasi Data", "smt": 3, "sks": 3},
    {"kode": "14823383", "nama": "Manajemen Data dan Keamanan Siber", "smt": 3, "sks": 3},
    {"kode": "14823032", "nama": "Manajemen Sistem Informasi", "smt": 3, "sks": 2},
    {"kode": "1003124202", "nama": "Pendidikan Agama Islam", "smt": 3, "sks": 2},
    {"kode": "1003124102", "nama": "Pendidikan Pancasila", "smt": 3, "sks": 2},
    {"kode": "14823293", "nama": "Pengembangan Sistem Berbasis Web", "smt": 3, "sks": 3},
    {"kode": "14823083", "nama": "Rekayasa Kebutuhan Perangkat Lunak", "smt": 3, "sks": 3},
    {"kode": "14823123", "nama": "Sistem Enterprise", "smt": 3, "sks": 3},
]

BOBOT = {"A": 4, "AB": 3.5, "B": 3, "BC": 2.5, "C": 2, "D": 1, "E": 0}


def hitung_total_sks(data):
    return sum(mk["sks"] for mk in data)


def hitung_ipk(data):
    total_sks = hitung_total_sks(data)
    if total_sks == 0:
        return 0
    return sum(BOBOT[mk["nilai"]] * mk["sks"] for mk in data) / total_sks


def nilai_dengan_nk(data):
    """Salinan data + kolom N.K. (bobot x sks) agar template tidak perlu menghitung."""
    return [{**mk, "nk": BOBOT[mk["nilai"]] * mk["sks"]} for mk in data]


# Tempat menyimpan pesan dari form kontak (hilang saat server restart, cukup untuk demo)
pesan_masuk = []
