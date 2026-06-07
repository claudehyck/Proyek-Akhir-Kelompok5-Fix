# =============================================================
# MAIN PROGRAM
# =============================================================
def main():
    app = AppPlanner()

    while True:

        print("\n=== SMART TRAVEL PLANNER ===")
        print("1. Tambah Destinasi")
        print("2. Sorting Destinasi")
        print("3. Searching Destinasi")
        print("4. Simpan File")
        print("5. Load File")
        print("6. Hitung Total Biaya")
        print("7. Undo Destinasi")
        print("8. Antrean Tiket")
        print("9. Jadwal Kunjungan")
        print("10. Galeri Foto")
        print("11. Slideshow")
        print("12. Tree Kategori")
        print("13. Graph Jalur")
        print("14. Validasi Tiket")
        print("0. Keluar")

        pilih = input("\nPilih Menu: ")

        # =====================================================
        # TAMBAH DESTINASI
        # =====================================================
        if pilih == "1":
            nama = input("Nama Destinasi: ")
            
            # 1. Validasi Rating
            while True:
                try:
                    rating = float(input("Rating (0-10): "))
                    if not (0 <= rating <= 10):
                        print("Rating harus dari 0-10 ! ")
                        continue
                    break
                except ValueError:
                    print("rating harus berupa angka!")
            
            # 2. Validasi Tiket
            while True:
                try:
                    tiket = int(input("Biaya Tiket: "))
                    if tiket < 0:
                        print("Biaya tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("Biaya harus berupa angka bulat! Contoh: 50000")
            
            # 3. Validasi Hotel
            while True:
                try:
                    hotel = int(input("Biaya Hotel: "))
                    if hotel < 0:
                        print("Biaya tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("Biaya harus berupa angka bulat! Contoh: 50000")
            
            # 4. Validasi Makan
            while True:
                try:
                    makan = int(input("Biaya Makan: "))
                    if makan < 0:
                        print("Biaya tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("Biaya harus berupa angka bulat! Contoh: 50000")
                    
            # 5. Pilihan Kategori
            print("\nKategori:")
            print("1. Alam")
            print("2. Budaya")
            print("3. Kuliner")

            pilih_kat = input("Pilih: ")

            if pilih_kat == "1":
                kat = "Alam"
            elif pilih_kat == "2":
                kat = "Budaya"
            else:
                kat = "Kuliner"

            # 6. Input Koordinat (PASTIKAN DI SINI, DI LUAR LOOP BIAYA)
            while True:
                try:
                    lat = input("Latitude (-90 s/d 90): ")
                    lat = float(lat)
                    if lat < -90 or lat > 90:
                        print("Latitude harus antara -90 sampai 90!")
                        continue
                    break

                except ValueError:
                    print("Latitude harus berupa angka!")

            while True:
                try:

                    lon = input("Longitude (-180 s/d 180): ")
                    lon = float(lon)

                    if lon < -180 or lon > 180:
                        print("Longitude harus antara -180 sampai 180!")
                        continue

                    break

                except ValueError:
                    print("Longitude harus berupa angka!")

            # 7. Memasukkan data ke Objek Destinasi dan Struktur Data
            d = Destinasi(
                nama,
                rating,
                tiket,
                hotel,
                makan,
                {kat},
                (lat, lon)
            )

            app.db.append(d)
            app.sll.add(nama)
            app.dll.add(f"Foto_{nama}.jpg")
            app.cll.add(nama)
            app.stack_undo.append(nama)

            if kat not in app.kategori_terdaftar:
                node_kat = CategoryTree(kat)
                app.root_cat.add_child(node_kat)
                app.kategori_terdaftar[kat] = node_kat

            app.kategori_terdaftar[kat].add_child(CategoryTree(nama))

            print("Destinasi berhasil ditambahkan!")

        # =====================================================
        # SORTING
        # =====================================================
        elif pilih == "2":

            print("\n1. Rating Tertinggi")
            print("2. Biaya Termurah")

            s = input("Pilih: ")

            if s == "1":
                app.sort_rating()

                print("\nHasil Sorting Rating:")

                for d in app.db:
                    print(f"{d.nama} | Rating: {d.rating}")

            elif s == "2":
                app.sort_biaya()

                print("\nHasil Sorting Biaya:")

                for d in app.db:
                    print(f"{d.nama} | Biaya: Rp{d.biaya}")

        # =====================================================
        # SEARCHING
        # =====================================================
        elif pilih == "3":

            key = input("Cari Destinasi: ")

            hasil = app.cari_destinasi(key)

            if hasil:

                for d in hasil:

                    print("\n===================")
                    print(f"Nama      : {d.nama}")
                    print(f"Rating    : {d.rating}")
                    print(f"Biaya     : Rp{d.biaya}")
                    print(f"Kategori  : {d.kategori}")
                    print(f"Koordinat : {d.koordinat}")

            else:
                print("Destinasi tidak ditemukan.")

        # =====================================================
        # SAVE FILE
        # =====================================================
        elif pilih == "4":

            with open("itinerary.txt", "w") as f:

                for d in app.db:

                    f.write(f"{d.nama}|")
                    f.write(f"{d.rating}|")
                    f.write(f"{d.biaya}\n")

            print("Data berhasil disimpan.")

        # =====================================================
        # LOAD FILE
        # =====================================================
        elif pilih == "5":

            try:
                with open("itinerary.txt", "r") as f:

                    print("\n=== DATA FILE ===")

                    for line in f:
                        print(line.strip())

            except:
                print("File belum ada!")

        # =====================================================
        # REKURSIF
        # =====================================================
        elif pilih == "6":

            total = app.hitung_biaya_rekursif(len(app.db))

            print(f"\nTotal Biaya Perjalanan: Rp{total}")

        # =====================================================
        # STACK
        # =====================================================
        elif pilih == "7":

            if app.undo_destinasi():
                print("Undo berhasil!")
            else:
                print("Tidak ada data.")

                # =====================================================
        # QUEUE
        # =====================================================
        elif pilih == "8":

            print("\n=== ANTREAN TIKET ===")
            print("1. Tambah Antrean")
            print("2. Proses Antrean")
            print("3. Lihat Antrean")

            q = input("Pilih: ")

            # Tambah antrean
            if q == "1":

                nama = input("Nama Turis: ")

                app.queue_tiket.enqueue(nama)

                print(f"{nama} masuk antrean!")

            # Proses antrean
            elif q == "2":

                proses = app.queue_tiket.dequeue()

                if proses:
                    print(f"Tiket {proses} diproses!")
                else:
                    print("Antrean kosong!")

            # Lihat antrean
            elif q == "3":

                antrean = app.queue_tiket.display()

                if antrean:
                    print("Daftar Antrean:")
                    for i, nama in enumerate(antrean, start=1):
                        print(f"{i}. {nama}")
                else:
                    print("Belum ada antrean.")

            else:
                print("Pilihan tidak valid!")

        # =====================================================
        # SINGLE LINKED LIST
        # =====================================================
        elif pilih == "9":

            print("\nJadwal:")
            print(app.sll.display())

        # =====================================================
        # DOUBLE LINKED LIST
        # =====================================================
        elif pilih == "10":

            if app.dll.current:

                print(f"\nFoto Saat Ini: {app.dll.current.data}")

                nav = input("n/p: ")

                if nav == "n":

                    if app.dll.current.next:
                        app.dll.current = app.dll.current.next

                elif nav == "p":

                    if app.dll.current.prev:
                        app.dll.current = app.dll.current.prev

                print("Sekarang:", app.dll.current.data)

        # =====================================================
        # CIRCULAR LINKED LIST
        # =====================================================
        elif pilih == "11":

            if app.cll.head:

                curr = app.cll.head

                print("\nSlideshow:")

                for i in range(5):
                    print(curr.data)
                    curr = curr.next

        # =====================================================
        # TREE
        # =====================================================
        elif pilih == "12":

            print("\n=== TREE KATEGORI ===")

            print(app.root_cat.name)

            for cat in app.root_cat.children:

                print(f" ├── {cat.name}")

                for tempat in cat.children:

                    print(f" │    ├── {tempat.name}")

        # =====================================================
        # GRAPH
        # =====================================================
        elif pilih == "13":

            if len(app.db) >= 2:

            # RESET GRAPH AGAR TIDAK DUPLIKAT
                app.graph = TravelGraph()

                for i in range(len(app.db)-1):
                    asal = app.db[i].nama
                    tujuan = app.db[i+1].nama

                    jarak = int(input(
                    f"Jarak {asal} ke {tujuan} (KM): "
                ))

                app.graph.add_edge(
                    asal,
                    tujuan,
                    jarak
            )

                print("\n=== GRAPH ===")

                for asal, tujuan in app.graph.adj.items():

                    print(f"{asal} --> {tujuan}")

            else:
                print("Minimal 2 destinasi.")
            
        # =====================================================
        # HASH TABLE
        # =====================================================
        elif pilih == "14":

            tid = input("Masukkan ID Tiket: ")

            app.hash_tix.insert(tid)

            cek = input("Cek ID Tiket: ")

            if app.hash_tix.check(cek):
                print("VALID")
            else:
                print("TIDAK VALID")

        # =====================================================
        # EXIT
        # =====================================================
        elif pilih == "0":

            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# =============================================================
# ENTRY POINT
# =============================================================
if __name__ == "__main__":
    main()