class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_to_tail(self, number):
        new_node = Node(number)

        if self.tail:
            cur_node = self.head
            next_node = self.head.next 
            while next_node is not self.tail:
                cur_node = cur_node.next
                new_node = new_node.next
            next_node.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = self.head 
            