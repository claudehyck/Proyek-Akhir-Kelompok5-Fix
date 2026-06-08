# =========================================================
# REKURSIF — Hitung Total Biaya
# Menjumlahkan biaya semua destinasi secara rekursif.
# Base case: jika n=0, kembalikan 0.
# Rekursif: biaya destinasi ke-n + jumlah semua sebelumnya.
# =========================================================
def hitung_biaya_rekursif(self, n):
    if n == 0:
        return 0   # Base case: tidak ada destinasi

    # Langsung ambil properti .biaya dari objek Destinasi
    return self.db[n-1].biaya + self.hitung_biaya_rekursif(n-1)
