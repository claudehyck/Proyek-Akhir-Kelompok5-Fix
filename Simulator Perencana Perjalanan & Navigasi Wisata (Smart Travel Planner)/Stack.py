# =========================================================
# UNDO DESTINASI
# Menghapus destinasi terakhir dari semua struktur data
# =========================================================
def undo_destinasi(self):

    # Jika stack kosong
    if not self.stack_undo:
        return False

    # Ambil destinasi terakhir (LIFO)
    nama_hapus = self.stack_undo.pop()

    # =====================================================
    # HAPUS DARI DATABASE
    # =====================================================
    for i in range(len(self.db)-1, -1, -1):

        if self.db[i].nama == nama_hapus:
            self.db.pop(i)
            break

    # =====================================================
    # HAPUS DARI SINGLE LINKED LIST
    # =====================================================
    self.sll.remove_last()

    # =====================================================
    # HAPUS DARI DOUBLE LINKED LIST
    # =====================================================
    self.dll.remove_last()

    # =====================================================
    # HAPUS DARI CIRCULAR LINKED LIST
    # =====================================================
    self.cll.remove_last()

    # =====================================================
    # HAPUS DARI TREE
    # =====================================================
    for kategori in self.root_cat.children:

        for child in kategori.children:

            if child.name == nama_hapus:

                kategori.children.remove(child)
                break

    # =====================================================
    # HAPUS KATEGORI KOSONG
    # =====================================================
    kategori_hapus = []

    for kategori in self.root_cat.children:

        if len(kategori.children) == 0:
            kategori_hapus.append(kategori)

    for k in kategori_hapus:
        self.root_cat.children.remove(k)

    # =====================================================
    # RESET GRAPH
    # =====================================================
    self.graph = TravelGraph()

    return True