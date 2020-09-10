"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../stack/')
from stack import Stack

import sys
sys.path.append('../singly_linked_list/')

from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0;
        self.storage = LinkedList()
        
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    #add value as new node to the right of the current (self) node
    def __add_right__(self, value):
        self.right = BSTNode(value)
        
    #add value as new node to the left of the current (self) node
    def __add_left__(self, value):
        self.left = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        #check if value is >= to the current node
        if value < self.value:
            #check if left node space is open
            if not self.left:
                #add new node to left
                self.__add_left__(value)
            else:
                #check the value of the left node to the value we want to insert
                self.left.insert(value)
        else:
            #check if right node space is open
            if not self.right:
                #add new node to right 
                self.__add_right__(value)
            else:
                #check the value of the right node to the value we want to insert 
                self.right.insert( value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        while self.value != target:
            #check left side of node
            if self.value > target:
                #if there is a left child node set the self to the child and loop again
                if self.left:
                    self = self.left
                else:
                    return False
            #check right side of node
            else:
                #if there is a right child node set the self to the child node and loop again
                if self.right:
                    self = self.right
                else:
                    return False
        return True
                

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        
        while self.right:
            self = self.right
        
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        pass
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #create empty queue
        q = Queue()
        #enqueue starting node
        q.enqueue(self)
        #while queue is not empty
        while q.size != 0:
            #dequeue the current node
            current = q.dequeue()
            #print the node's value
            print(current.value)
            #if left child
            if current.left:
                #enqueue the left child
                q.enqueue(current.left)
            #if right child
            if current.right:
                #enquque the right child
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #create an empty stack
        stack = Stack()
        #push starting node on stack
        stack.push(self)
        #while stack is not empty
        while stack.size != 0:
            #pop the current node
            current = stack.pop()
            #print the value
            print(current.value)
            #if node has left child push left child onto stack
            if current.left:
                stack.push(current.left)
            #if node has right child push right child onto stack
            if current.right:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
