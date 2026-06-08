# =============================================================
# APP PLANNER
# Kelas utama yang menggabungkan SEMUA struktur data dan fitur.
# Objek 'app' dibuat sekali di main(), lalu dipakai sepanjang program.
# =============================================================
class AppPlanner:
    def __init__(self):
        self.db = []               # Database utama: list semua objek Destinasi

        self.stack_undo = []       # Stack untuk fitur undo (LIFO)
        self.queue_tiket = TicketQueue()   # Antrian tiket wisata

        self.sll = ItinerarySLL()  # Single Linked List untuk jadwal kunjungan
        self.dll = PhotoDLL()      # Double Linked List untuk galeri foto
        self.cll = SlideshowCLL()  # Circular Linked List untuk slideshow

        self.graph = TravelGraph() # Graf jalur antar destinasi
        self.hash_tix = TicketHash()  # Hash table untuk validasi tiket

        self.root_cat = CategoryTree("Wisata")   # Root dari pohon kategori

        self.kategori_terdaftar = {}   # Dict: {nama_kategori: node_tree} agar tidak duplikat