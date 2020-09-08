class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.length = 0


class LinkedList:
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
        self.length += 1

    # remove
    def remove_head(self):
        # check if list is empty
        if not self.head:
            # return none
            return None
        # check if list has one element
        elif self.head == self.tail:  # or self.length == 1 if implemented
            # set self.head to current_head.next (which is None)
            current_head = self.head
            self.head = None
            # set self.tail to None
            self.tail = None
            # decrease length by 1
            self.length -= 1
            return current_head.value
        else:
            # set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            # return current_head value
            return current_head.value

    def remove_tail(self):
        pass
