# =========================================================
# SEARCHING
# =========================================================
def cari_destinasi(self, keyword):
    hasil = []

    for d in self.db:
        if keyword.lower() in d.nama.lower():
            hasil.append(d)

    return hasil