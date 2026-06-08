# =========================================================
# SEARCHING — Linear Search
# Cari destinasi yang namanya mengandung keyword tertentu.
# Tidak case-sensitive karena pakai .lower() di kedua sisi.
# =========================================================
def cari_destinasi(self, keyword):
    hasil = []

    for d in self.db:
        if keyword.lower() in d.nama.lower():
            hasil.append(d)   # Masukkan ke hasil jika cocok

    return hasil   # Kembalikan list hasil pencarian