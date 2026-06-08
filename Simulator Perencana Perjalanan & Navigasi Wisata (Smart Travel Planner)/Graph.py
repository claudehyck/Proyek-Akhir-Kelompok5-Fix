# =============================================================
# GRAPH
# Digunakan untuk memetakan jalur antar destinasi beserta jaraknya.
# Menggunakan adjacency list: setiap kota menyimpan list tetangganya.
# Graf ini TIDAK BERARAH (undirected): A->B otomatis B->A juga.
# =============================================================
class TravelGraph:
    def __init__(self):
        self.adj = {}   # Dictionary: {kota: [(tetangga, jarak), ...]}

    def add_edge(self, u, v, jarak):
        # Tambah jalur dua arah antara u dan v dengan jarak tertentu
        if u not in self.adj:
            self.adj[u] = []   # Inisialisasi list tetangga untuk u

        if v not in self.adj:
            self.adj[v] = []   # Inisialisasi list tetangga untuk v

        self.adj[u].append((v, jarak))   # u bisa ke v sejauh 'jarak'
        self.adj[v].append((u, jarak))   # v juga bisa ke u (dua arah)