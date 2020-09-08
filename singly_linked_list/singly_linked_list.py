class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None  # points to first node in the list
        self.tail = None  # points to last node in the list

    # append
    def add_to_tail(self, value):
        # create a new node
        new_tail = Node(value, None)
        # check if list is empty
        if not self.tail:
            # set self.head and self.tail to new node
            self.head = new_tail
            self.tail = new_tail
        else:
            # set current tail to new node
            old_tail = self.tail
            old_tail.next = new_tail
            # set self.tail to new node
            self.tail = new_tail

    # remove
    def remove_head(self):
        pass

    def remove_tail(self):
        pass
