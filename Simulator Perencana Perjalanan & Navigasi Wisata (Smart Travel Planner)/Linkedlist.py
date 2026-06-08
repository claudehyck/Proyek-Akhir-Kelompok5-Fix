#=============================================================
# SMART TRAVEL PLANNER
#============================================================

# =============================================================
# NODE
# Ini adalah "kotak" dasar untuk semua Linked List.
# Setiap node menyimpan data, pointer ke node berikutnya (next),
# dan pointer ke node sebelumnya (prev) untuk Double Linked List.
# =============================================================
class Node:
    def __init__(self, data):
        self.data = data   # Isi/nilai dari node ini
        self.next = None   # Pointer ke node berikutnya (default kosong)
        self.prev = None   # Pointer ke node sebelumnya (dipakai di DLL)


# =============================================================
# SINGLE LINKED LIST (SLL)
# Digunakan untuk menyimpan jadwal itinerary (urutan kunjungan).
# Setiap node hanya tahu node BERIKUTNYA (satu arah ->).
# =============================================================
class ItinerarySLL:
    def __init__(self):
        self.head = None   # Awal list, awalnya kosong

    def add(self, data):
        # Tambah node baru di paling AKHIR list
        new_node = Node(data)

        if not self.head:
            # Jika list masih kosong, node baru langsung jadi head
            self.head = new_node
        else:
            # Kalau sudah ada isi, jalan terus sampai node terakhir
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node   # Sambungkan node terakhir ke node baru

    def remove_last(self):
        # Hapus node paling AKHIR dari list (dipakai saat undo)
        if not self.head:
            return   # List kosong, tidak ada yang dihapus

        if not self.head.next:
            # Hanya ada 1 node, langsung kosongkan head
            self.head = None
            return

        # Jalan sampai node sebelum yang terakhir
        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None   # Putus sambungan ke node terakhir

    def display(self):
        # Tampilkan semua node dalam format: A -> B -> C
        curr = self.head
        result = []

        while curr:
            result.append(curr.data)
            curr = curr.next

        return " -> ".join(result) if result else "Kosong"


# =============================================================
# DOUBLE LINKED LIST (DLL)
# Digunakan untuk galeri foto. Bisa navigasi MAJU (next) dan
# MUNDUR (prev) — dua arah <- ->.
# =============================================================
class PhotoDLL:
    def __init__(self):
        self.head = None      # Node pertama
        self.current = None   # Node yang sedang aktif/ditampilkan

    def add(self, img):
        # Tambah foto baru di paling akhir list
        new_node = Node(img)

        if not self.head:
            # List kosong, node baru jadi head
            self.head = new_node
        else:
            # Jalan ke node paling akhir
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node    # Sambung node terakhir ke node baru
            new_node.prev = curr    # Sambung balik (inilah yang bikin "double")

        if self.current is None:
            # Pertama kali ada foto, set current ke head
            self.current = self.head

    def remove_last(self):
        # Hapus foto terakhir dari galeri (dipakai saat undo)
        if not self.head:
            return

        if not self.head.next:
            # Hanya 1 foto, kosongkan semua
            self.head = None
            self.current = None
            return

        # Jalan ke node paling akhir
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.prev.next = None   # Putus sambungan dari node sebelumnya ke node terakhir
        self.current = self.head   # Reset tampilan ke foto pertama


# =============================================================
# CIRCULAR LINKED LIST (CLL)
# Digunakan untuk slideshow. Node terakhir menyambung KEMBALI
# ke node pertama, sehingga bisa berputar terus tanpa henti.
# =============================================================
class SlideshowCLL:
    def __init__(self):
        self.head = None   # Node pertama

    def add(self, item):
        # Tambah item baru ke CLL
        new_node = Node(item)

        if not self.head:
            # List kosong: node pertama next-nya ke dirinya sendiri (melingkar)
            self.head = new_node
            new_node.next = self.head
        else:
            # Jalan sampai node yang next-nya kembali ke head (node terakhir)
            curr = self.head

            while curr.next != self.head:
                curr = curr.next

            curr.next = new_node       # Node terakhir lama -> node baru
            new_node.next = self.head  # Node baru -> kembali ke head (melingkar)

    def remove_last(self):
        # Hapus node terakhir dari CLL (dipakai saat undo)
        if not self.head:
            return

        if self.head.next == self.head:
            # Hanya 1 node, kosongkan list
            self.head = None
            return

        # Jalan sampai node sebelum node terakhir
        curr = self.head

        while curr.next.next != self.head:
            curr = curr.next

        curr.next = self.head   # Sambungkan node sebelum-terakhir langsung ke head