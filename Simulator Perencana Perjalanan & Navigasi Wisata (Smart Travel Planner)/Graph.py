# =============================================================
# GRAPH
# =============================================================
class TravelGraph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, jarak):
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, jarak))
        self.adj[v].append((u, jarak))