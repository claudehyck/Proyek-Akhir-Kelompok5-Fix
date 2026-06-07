# =========================================================
# REKURSIF
# =========================================================
def hitung_biaya_rekursif(self, n):
    if n == 0:
        return 0
    # Langsung ambil properti .biaya dari objek Destinasi
    return self.db[n-1].biaya + self.hitung_biaya_rekursif(n-1)