# =============================================================
# APP PLANNER
# =============================================================
class AppPlanner:
    def __init__(self):
        self.db = []

        self.stack_undo = []
        self.queue_tiket = TicketQueue()

        self.sll = ItinerarySLL()
        self.dll = PhotoDLL()
        self.cll = SlideshowCLL()

        self.graph = TravelGraph()
        self.hash_tix = TicketHash()

        self.root_cat = CategoryTree("Wisata")

        self.kategori_terdaftar = {}