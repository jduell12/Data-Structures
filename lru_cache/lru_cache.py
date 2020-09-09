import sys
sys.path.append('../doubly_linked_list/')

from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it can hold, the current number of nodes it is holding, a doubly-linked list that holds the key-value entries in the correct order, as well as a storage dict that provides fast access to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.dlist = None 
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #checks if key is in the dictionary
        if key in self.storage:
           current_node = self.dlist.head
           count = 0
           while count < self.limit:
               if current_node:
                  if current_node.value == key:
                      break
                  else:
                      current_node = current_node.next
               count += 1
           #move node to front
           self.dlist.move_to_front(current_node)
           return self.storage[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
           self.storage[key] = value 
           #move the node to the front 
           current_node = self.dlist.head
           while current_node != None:
               if current_node.value == key:
                   break
               else:
                   current_node = current_node.next
        else:
            #checks if cache is empty
            if self.current == 0:
                #creates a new doubly linked list
                self.dlist = DoublyLinkedList(ListNode(key))
                #adds the key value pair to the dictionary
                self.storage[key] = value 
                self.current += 1
            #check if cache is full
            elif self.current == self.limit:
                #removes tail from the doubly linked list
                removedKey = self.dlist.remove_from_tail()
                #removes key and value from dictionary
                del self.storage[removedKey]
                #adds key to the front of the doubly linked list
                self.dlist.add_to_head(key)
                #adds the key value pair to the dictionary
                self.storage[key] = value 
            else:
                #adds key to the front of the doubly linked list
                self.dlist.add_to_head(key)
                #adds the key value pair to the dictionary
                self.storage[key] = value 
                self.current += 1