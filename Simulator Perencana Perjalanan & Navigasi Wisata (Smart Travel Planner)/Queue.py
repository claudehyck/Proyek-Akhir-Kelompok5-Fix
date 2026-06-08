# =============================================================
# QUEUE (Antrian)
# Digunakan untuk antrian tiket wisata.
# Prinsip FIFO: yang masuk pertama, keluar/diproses pertama.
# =============================================================
class TicketQueue:
    def __init__(self):
        self.queue = []   # List biasa sebagai wadah antrian

    # Tambah antrean
    def enqueue(self, data):
        # Masukkan orang baru ke BELAKANG antrian
        self.queue.append(data)

    # Proses antrean pertama
    def dequeue(self):
        # Keluarkan orang paling DEPAN antrian (FIFO)
        if not self.is_empty():
            return self.queue.pop(0)   # pop(0) ambil elemen pertama
        return None

    # Cek kosong
    def is_empty(self):
        # Kembalikan True jika antrian kosong
        return len(self.queue) == 0

    # Tampilkan antrean
    def display(self):
        # Kembalikan seluruh isi antrian
        return self.queue