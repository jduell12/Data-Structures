class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None  # points to first node in the list
        self.tail = None  # points to last node in the list
