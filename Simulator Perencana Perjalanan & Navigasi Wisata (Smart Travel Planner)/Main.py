# =============================================================
# MAIN PROGRAM
# Fungsi utama: membuat objek AppPlanner dan menampilkan menu
# berulang (loop) sampai user memilih keluar (0).
# =============================================================
def main():
    app = AppPlanner()   # Buat satu objek AppPlanner yang dipakai sepanjang program

    while True:   # Loop terus sampai user pilih "0" (keluar)

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

        pilih = input("\nPilih Menu: ")   # Tampung pilihan user

        # =====================================================
        # TAMBAH DESTINASI
        # Input semua data destinasi dengan validasi, lalu simpan
        # ke semua struktur data sekaligus (db, sll, dll, cll, tree, stack)
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
            # Validasi latitude: harus float antara -90 s/d 90
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

            # Validasi longitude: harus float antara -180 s/d 180
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
            # Buat objek Destinasi baru dari semua input yang sudah divalidasi
            d = Destinasi(
                nama,
                rating,
                tiket,
                hotel,
                makan,
                {kat},          # Set berisi satu kategori
                (lat, lon)      # Tuple koordinat
            )

            app.db.append(d)               # Simpan ke database utama (list)
            app.sll.add(nama)              # Tambah nama ke Single Linked List (jadwal)
            app.dll.add(f"Foto_{nama}.jpg") # Tambah foto ke Double Linked List (galeri)
            app.cll.add(nama)              # Tambah ke Circular Linked List (slideshow)
            app.stack_undo.append(nama)    # Push ke stack untuk keperluan undo

            # Tambah ke Tree Kategori jika kategori belum ada
            if kat not in app.kategori_terdaftar:
                node_kat = CategoryTree(kat)
                app.root_cat.add_child(node_kat)         # Sambungkan ke root
                app.kategori_terdaftar[kat] = node_kat   # Daftarkan di dict

            # Tambah nama destinasi sebagai anak dari node kategorinya
            app.kategori_terdaftar[kat].add_child(CategoryTree(nama))

            print("Destinasi berhasil ditambahkan!")

        # =====================================================
        # SORTING
        # Pilih sorting berdasarkan rating (desc) atau biaya (asc)
        # =====================================================
        elif pilih == "2":

            print("\n1. Rating Tertinggi")
            print("2. Biaya Termurah")

            s = input("Pilih: ")

            if s == "1":
                app.sort_rating()   # Panggil bubble sort rating (descending)

                print("\nHasil Sorting Rating:")

                for d in app.db:
                    print(f"{d.nama} | Rating: {d.rating}")

            elif s == "2":
                app.sort_biaya()   # Panggil bubble sort biaya (ascending)

                print("\nHasil Sorting Biaya:")

                for d in app.db:
                    print(f"{d.nama} | Biaya: Rp{d.biaya}")

        # =====================================================
        # SEARCHING
        # Cari destinasi berdasarkan kata kunci nama (linear search)
        # =====================================================
        elif pilih == "3":

            key = input("Cari Destinasi: ")

            hasil = app.cari_destinasi(key)   # Kembalikan list hasil pencarian

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
        # Simpan semua destinasi ke file teks "itinerary.txt"
        # Format tiap baris: nama|rating|biaya
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
        # Baca dan tampilkan isi file "itinerary.txt"
        # Jika file belum ada, tampilkan pesan error
        # =====================================================
        elif pilih == "5":

            try:
                with open("itinerary.txt", "r") as f:

                    print("\n=== DATA FILE ===")

                    for line in f:
                        print(line.strip())   # strip() hilangkan newline di akhir baris

            except:
                print("File belum ada!")

        # =====================================================
        # REKURSIF
        # Hitung total biaya semua destinasi menggunakan fungsi rekursif
        # =====================================================
        elif pilih == "6":

            total = app.hitung_biaya_rekursif(len(app.db))   # Mulai dari destinasi terakhir

            print(f"\nTotal Biaya Perjalanan: Rp{total}")

        # =====================================================
        # STACK (UNDO)
        # Hapus destinasi terakhir yang ditambahkan dari semua struktur data
        # Prinsip LIFO: yang terakhir masuk, pertama keluar
        # =====================================================
        elif pilih == "7":

            if app.undo_destinasi():
                print("Undo berhasil!")
            else:
                print("Tidak ada data.")

                # =====================================================
        # QUEUE (Antrian Tiket)
        # Kelola antrian tiket wisata: tambah, proses, atau lihat antrian
        # =====================================================
        elif pilih == "8":

            print("\n=== ANTREAN TIKET ===")
            print("1. Tambah Antrean")
            print("2. Proses Antrean")
            print("3. Lihat Antrean")

            q = input("Pilih: ")

            # Tambah antrean: masukkan nama turis ke belakang antrian
            if q == "1":

                nama = input("Nama Turis: ")

                app.queue_tiket.enqueue(nama)   # FIFO: masuk dari belakang

                print(f"{nama} masuk antrean!")

            # Proses antrean: keluarkan turis paling depan
            elif q == "2":

                proses = app.queue_tiket.dequeue()   # FIFO: keluar dari depan

                if proses:
                    print(f"Tiket {proses} diproses!")
                else:
                    print("Antrean kosong!")

            # Lihat antrean: tampilkan seluruh isi antrian saat ini
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
        # Tampilkan jadwal kunjungan dalam format A -> B -> C
        # =====================================================
        elif pilih == "9":

            print("\nJadwal:")
            print(app.sll.display())   # Panggil method display() dari SLL

        # =====================================================
        # DOUBLE LINKED LIST (Galeri Foto)
        # Navigasi foto ke depan (n) atau ke belakang (p)
        # Bisa dua arah karena DLL punya pointer next DAN prev
        # =====================================================
        elif pilih == "10":

            if app.dll.current:

                print(f"\nFoto Saat Ini: {app.dll.current.data}")

                nav = input("n/p: ")   # n = next (maju), p = prev (mundur)

                if nav == "n":

                    if app.dll.current.next:
                        app.dll.current = app.dll.current.next   # Geser ke foto berikutnya

                elif nav == "p":

                    if app.dll.current.prev:
                        app.dll.current = app.dll.current.prev   # Geser ke foto sebelumnya

                print("Sekarang:", app.dll.current.data)

        # =====================================================
        # CIRCULAR LINKED LIST (Slideshow)
        # Tampilkan 5 item berurutan. Karena melingkar, setelah
        # item terakhir otomatis kembali ke item pertama.
        # =====================================================
        elif pilih == "11":

            if app.cll.head:

                curr = app.cll.head

                print("\nSlideshow:")

                for i in range(5):       # Tampilkan 5 item
                    print(curr.data)
                    curr = curr.next     # Setelah node terakhir otomatis kembali ke head

        # =====================================================
        # TREE
        # Tampilkan struktur pohon kategori dalam format teks
        # Root -> Kategori -> Destinasi
        # =====================================================
        elif pilih == "12":

            print("\n=== TREE KATEGORI ===")

            print(app.root_cat.name)   # Cetak root: "Wisata"

            for cat in app.root_cat.children:

                print(f" ├── {cat.name}")   # Cetak kategori (Alam/Budaya/Kuliner)

                for tempat in cat.children:

                    print(f" │    ├── {tempat.name}")   # Cetak nama destinasi

        # =====================================================
        # GRAPH
        # Bangun graf jalur antar destinasi berdasarkan input jarak user.
        # Setiap pasang destinasi berurutan dihubungkan dengan satu edge.
        # =====================================================
        elif pilih == "13":

            if len(app.db) >= 2:   # Minimal 2 destinasi untuk membuat edge

            # RESET GRAPH AGAR TIDAK DUPLIKAT
                app.graph = TravelGraph()   # Buat ulang graf kosong sebelum diisi ulang

                for i in range(len(app.db)-1):
                    asal = app.db[i].nama
                    tujuan = app.db[i+1].nama

                    # Minta user input jarak antara dua destinasi berurutan
                    jarak = int(input(
                    f"Jarak {asal} ke {tujuan} (KM): "
                ))

                app.graph.add_edge(
                    asal,
                    tujuan,
                    jarak
            )

                print("\n=== GRAPH ===")

                # Tampilkan adjacency list: setiap kota dan tetangganya
                for asal, tujuan in app.graph.adj.items():

                    print(f"{asal} --> {tujuan}")

            else:
                print("Minimal 2 destinasi.")
            
        # =====================================================
        # HASH TABLE (Validasi Tiket)
        # Simpan ID tiket ke hash table, lalu cek apakah ID lain valid
        # =====================================================
        elif pilih == "14":

            tid = input("Masukkan ID Tiket: ")

            app.hash_tix.insert(tid)   # Hash ID tiket dan simpan ke slot yang sesuai

            cek = input("Cek ID Tiket: ")

            # Cek apakah ID tiket yang dicari ada di hash table
            if app.hash_tix.check(cek):
                print("VALID")
            else:
                print("TIDAK VALID")

        # =====================================================
        # EXIT
        # Keluar dari loop while -> program selesai
        # =====================================================
        elif pilih == "0":

            print("Program selesai.")
            break   # Hentikan loop while True

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()