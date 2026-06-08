# =============================================================
# HASH TABLE
# Digunakan untuk validasi ID tiket secara cepat.
# ID tiket di-hash menjadi angka -> disimpan di slot tertentu.
# Pencarian O(1) rata-rata lebih cepat dari pencarian biasa.
# =============================================================
class TicketHash:
    def __init__(self):
        # Buat 10 slot (bucket) kosong untuk menyimpan tiket
        self.table = [[] for _ in range(10)]

    def _hash(self, key):
        # Fungsi hash: jumlahkan nilai ASCII semua karakter key,
        # lalu modulo 10 -> hasilnya pasti antara 0-9 (index slot)
        total = 0

        for c in str(key):
            total += ord(c)   # ord() = nilai ASCII karakter

        return total % 10   # Tentukan slot (0-9)

    def insert(self, tid):
        # Simpan ID tiket ke slot yang sesuai hasil hash
        slot = self._hash(tid)

        if tid not in self.table[slot]:
            # Hindari duplikat, baru tambahkan kalau belum ada
            self.table[slot].append(tid)

    def check(self, tid):
        # Cek apakah ID tiket ada di hash table
        slot = self._hash(tid)
        return tid in self.table[slot]   # True jika ditemukan