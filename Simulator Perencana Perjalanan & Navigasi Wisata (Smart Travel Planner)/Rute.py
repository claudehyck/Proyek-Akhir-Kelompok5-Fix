# =============================================================
# CLASS RUTE
# Blueprint untuk rute perjalanan antar destinasi.
# =============================================================
class Rute:
    def __init__(self, asal, tujuan, jarak):
        self.asal = asal       # Kota/destinasi asal
        self.tujuan = tujuan   # Kota/destinasi tujuan
        self.jarak = jarak     # Jarak dalam KM
