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
