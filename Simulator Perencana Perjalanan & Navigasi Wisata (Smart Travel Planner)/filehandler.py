# =========================================================
# SAVE FILE
# Menyimpan seluruh data destinasi ke file teks
# =========================================================
def save_file(self, nama_file="itinerary.txt"):
    # buka file mode write
    with open(nama_file, "w") as f:
        # looping semua data destinasi
        for d in self.db:
            # ambil kategori dari set
            kategori = list(d.kategori)[0]
            # susun data menjadi satu baris
            data = (
                f"{d.nama}|"
                f"{d.rating}|"
                f"{d.tiket}|"
                f"{d.hotel}|"
                f"{d.makan}|"
                f"{kategori}|"
                f"{d.koordinat[0]}|"
                f"{d.koordinat[1]}\n"
            )
            # tulis ke file
            f.write(data)
    return True