# =========================================================
# LOAD FILE
# Membaca file lalu memasukkan kembali data
# ke seluruh struktur data
# =========================================================
def load_file(self, nama_file="itinerary.txt"):

    try:

        # =============================================
        # RESET SEMUA DATA DULU
        # Agar tidak dobel saat load ulang
        # =============================================
        self.db = []

        self.sll = ItinerarySLL()
        self.dll = PhotoDLL()
        self.cll = SlideshowCLL()

        self.stack_undo = []

        self.root_cat = CategoryTree("Wisata")
        self.kategori_terdaftar = {}

        # =============================================
        # BACA FILE
        # =============================================
        with open(nama_file, "r") as f:

            for line in f:

                # Hilangkan enter lalu pisahkan berdasarkan |
                data = line.strip().split("|")

                # Ambil tiap data
                nama = data[0]
                rating = float(data[1])

                tiket = int(data[2])
                hotel = int(data[3])
                makan = int(data[4])

                kategori = data[5]

                lat = float(data[6])
                lon = float(data[7])

                # =====================================
                # BUAT OBJECT DESTINASI
                # =====================================
                d = Destinasi(
                    nama,
                    rating,
                    tiket,
                    hotel,
                    makan,
                    {kategori},
                    (lat, lon)
                )

                # =====================================
                # MASUKKAN KE DATABASE
                # =====================================
                self.db.append(d)

                # =====================================
                # MASUKKAN KE LINKED LIST
                # =====================================
                self.sll.add(nama)

                self.dll.add(f"Foto_{nama}.jpg")

                self.cll.add(nama)

                # =====================================
                # MASUKKAN KE STACK UNDO
                # =====================================
                self.stack_undo.append(nama)

                # =====================================
                # MASUKKAN KE TREE
                # =====================================
                if kategori not in self.kategori_terdaftar:

                    node_kat = CategoryTree(kategori)

                    self.root_cat.add_child(node_kat)

                    self.kategori_terdaftar[kategori] = node_kat

                self.kategori_terdaftar[kategori].add_child(
                    CategoryTree(nama)
                )

        return True

    except:
        return False