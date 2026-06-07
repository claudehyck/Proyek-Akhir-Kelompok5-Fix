# =========================================================
# SORTING RATING
# =========================================================
def sort_rating(self):
    for i in range(len(self.db)):
        for j in range(len(self.db)-1):

            if self.db[j].rating < self.db[j+1].rating:
                self.db[j], self.db[j+1] = self.db[j+1], self.db[j]

# =========================================================
# SORTING BIAYA
# =========================================================
def sort_biaya(self):
    for i in range(len(self.db)):
        for j in range(len(self.db)-1):

            if self.db[j].biaya > self.db[j+1].biaya:
                self.db[j], self.db[j+1] = self.db[j+1], self.db[j]