# =========================================================
# SORTING RATING — Bubble Sort (descending)
# Urutkan destinasi dari rating TERTINGGI ke terendah.
# Cara kerja: bandingkan dua elemen berdampingan, tukar jika terbalik.
# =========================================================
def sort_rating(self):
    for i in range(len(self.db)):
        for j in range(len(self.db)-1):
            # Jika rating kiri LEBIH KECIL dari kanan, tukar posisi
            if self.db[j].rating < self.db[j+1].rating:
                self.db[j], self.db[j+1] = self.db[j+1], self.db[j]

# =========================================================
# SORTING BIAYA — Bubble Sort (ascending)
# Urutkan destinasi dari biaya TERMURAH ke termahal.
# =========================================================
def sort_biaya(self):
    for i in range(len(self.db)):
        for j in range(len(self.db)-1):
            # Jika biaya kiri LEBIH BESAR dari kanan, tukar posisi
            if self.db[j].biaya > self.db[j+1].biaya:
                self.db[j], self.db[j+1] = self.db[j+1], self.db[j]