class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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
            return current_head.value
        else:
            # set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            # return current_head value
            return current_head.value

    def remove_tail(self):
        # check if list is empty
        if not self.head:
            # return none
            return None
        # check if one element in list
        elif self.head == self.tail:
            # save the current tail value
            current_tail = self.tail
            # set self.tail and self.head to None
            self.tail = None
            self.head = None
            # return the value of the node that was removed
            return current_tail.value
        else:
            # start at head and iterate to the next to last node
            last_node = self.head
            while last_node.next.next != None:
                last_node = last_node.next

            # save the current tail value
            old_tail = self.tail

            # set self.tail to current node
            self.tail = last_node

            # set current node next to None
            self.tail.next = None

            # return the value of the node that was removed
            return old_tail.value

    def printList(self):
        if not self.head:
            print('No items')
        else:
            last_node = self.head
            while last_node != self.tail:
                print(last_node.value)
                last_node = last_node.next
            print(last_node.value)
