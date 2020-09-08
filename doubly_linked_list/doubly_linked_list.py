"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create new node to add to list
        newNode = ListNode(value)
        # check if empty list
        if self.length == 0:
            #sets the prev and next to None
            newNode.next = None
            newNode.prev = None
            #makes the new node both head and tail since it's the only node in the list 
            self.head = newNode
            self.tail = newNode
        #check if only 1 element in list
        elif self.length == 1:
            #make new node the head
            self.head = newNode
            self.head.next = self.tail
            self.head.prev = None
            #make the tail point to the new head
            self.tail.prev = self.head
        else:
            #saves the old head node into a value
            old_head = self.head 
            #changes the new node to be the head
            self.head = newNode
            self.head.next = old_head
            self.head.prev = None
            #old head node previous link to the new head node
            old_head.prev = self.head
            
        #increments the length attribute after adding node to list
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass