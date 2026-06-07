# =============================================================
# CLASS DESTINASI
# =============================================================
class Destinasi:
    def __init__(self, nama, rating, tiket, hotel,
                 makan, kategori, koordinat):

        self.nama = nama
        self.rating = rating

        self.tiket = tiket
        self.hotel = hotel
        self.makan = makan

        self.biaya = tiket + hotel + makan

        self.kategori = kategori
        self.koordinat = koordinat

        self.fasilitas = {}