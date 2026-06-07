# =============================================================
# QUEUE
# =============================================================
class TicketQueue:
    def __init__(self):
        self.queue = []

    # Tambah antrean
    def enqueue(self, data):
        self.queue.append(data)

    # Proses antrean pertama
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    # Cek kosong
    def is_empty(self):
        return len(self.queue) == 0

    # Tampilkan antrean
    def display(self):
        return self.queue