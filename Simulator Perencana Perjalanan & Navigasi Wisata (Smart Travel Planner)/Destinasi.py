# =============================================================
# CLASS DESTINASI
# Blueprint/template untuk setiap destinasi wisata.
# Menyimpan semua info: nama, rating, biaya, kategori, koordinat.
# =============================================================
class Destinasi:
    def __init__(self, nama, rating, tiket, hotel,
                 makan, kategori, koordinat):

        self.nama = nama           # Nama destinasi
        self.rating = rating       # Rating 0-10

        self.tiket = tiket         # Biaya tiket masuk
        self.hotel = hotel         # Biaya hotel
        self.makan = makan         # Biaya makan

        self.biaya = tiket + hotel + makan   # Total biaya otomatis dihitung

        self.kategori = kategori       # Kategori: Alam/Budaya/Kuliner
        self.koordinat = koordinat     # Tuple (latitude, longitude)

        self.fasilitas = {}            # Dict fasilitas (kosong, siap diisi)