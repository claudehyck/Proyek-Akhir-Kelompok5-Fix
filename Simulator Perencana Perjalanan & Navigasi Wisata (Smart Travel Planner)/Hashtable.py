# =============================================================
# HASH TABLE
# =============================================================
class TicketHash:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def _hash(self, key):
        total = 0

        for c in str(key):
            total += ord(c)

        return total % 10

    def insert(self, tid):
        slot = self._hash(tid)

        if tid not in self.table[slot]:
            self.table[slot].append(tid)

    def check(self, tid):
        slot = self._hash(tid)
        return tid in self.table[slot]