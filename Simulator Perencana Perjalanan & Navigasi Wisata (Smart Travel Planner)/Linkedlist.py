# =============================================================
# SMART TRAVEL PLANNER
# =============================================================
# =============================================================
# NODE
# =============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# =============================================================
# SINGLE LINKED LIST
# =============================================================
class ItinerarySLL:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None

    def display(self):
        curr = self.head
        result = []

        while curr:
            result.append(curr.data)
            curr = curr.next

        return " -> ".join(result) if result else "Kosong"


# =============================================================
# DOUBLE LINKED LIST
# =============================================================
class PhotoDLL:
    def __init__(self):
        self.head = None
        self.current = None

    def add(self, img):
        new_node = Node(img)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

        if self.current is None:
            self.current = self.head

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.current = None
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.prev.next = None
        self.current = self.head


# =============================================================
# CIRCULAR LINKED LIST
# =============================================================
class SlideshowCLL:
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head

            while curr.next != self.head:
                curr = curr.next

            curr.next = new_node
            new_node.next = self.head

    def remove_last(self):
        if not self.head:
            return

        if self.head.next == self.head:
            self.head = None
            return

        curr = self.head

        while curr.next.next != self.head:
            curr = curr.next

        curr.next = self.head
