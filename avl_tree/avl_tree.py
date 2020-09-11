import sys
sys.path.append('../stack/')
from stack import Stack

"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Finds the number of nodes along the longest path from the root down to the farthest leaf node
    """
    def maxDepth(self):
        #get root node
        node = self.node
        #initialize left and right depths
        leftDepth = -1
        rightDepth = -1
        #if tree is empty return 0
        if not node:
            return 0
        else:
            #check for left child
            if node.left:
                #get the depth of left child
                leftDepth = node.left.maxDepth()
            #check for right child
            if node.right:
                #get depth of right child
                rightDepth = node.right.maxDepth()
        #find which depth is larger
        if leftDepth > rightDepth:
            return (leftDepth + 1)
        else:
            return (rightDepth + 1)
    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        self.height = self.maxDepth()

    """
    Updates the balance factor on the AVLTree class
    balance factor = height(left-child) - height(right-child)
    """
    def update_balance(self):
        balance = self.balance 
        
        if self.node.left and self.node.right:
            balance = self.node.left.maxDepth() - self.node.right.maxDepth()
        elif self.node.left:
            balance = self.node.left.maxDepth() - 0
        elif self.node.right:
            balance = 0 - self.node.right.maxDepth()
            
        self.balance = balance 

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        oldRoot = self.node 
        newRoot = self.node.right.node 
        if self.node.right.node.left:
            oldLeftChild = self.node.right.node.left.node
        
        #set new root as the root of the tree
        self.node = newRoot 
        #set the old root as the new root's left child
        self.node.left.node = oldRoot 
        #set the old left child of the new root as the right child of the new left child
        if self.node.right.node.left:
            self.node.left.node.right.node = oldLeftChild
        

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        oldRoot = self.node 
        newRoot = self.node.left.node 
        if self.node.left.node.right.node :
            oldRightChild = self.node.left.node.right.node 
        
        #set new root as the root of the tree
        self.node = newRoot
        #set the old root as the new root's right child 
        self.node.right.node = oldRoot
        #set the old left child of the new root as the leftchild of the new right child
        if self.node.left.node.right.node: 
            self.node.right.node.left.node = oldRightChild

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    balance factor = height(left-child) - height(right-child)
    """
    def rebalance(self):
        tree_height = self.maxDepth()
        #left left 
        if tree_height > 1 and self.node.key < self.node.left.node.key:
            self.right_rotate()
        #right right
        elif tree_height < -1 and self.node.key > self.node.right.node.key:
            self.left_rotate()
        #left right
        elif tree_height > 1 and self.node.key > self.node.left.node.key:
            self.node.left.left_rotate()
            self.right_rotate()
        #right left 
        elif tree_height < -1 and self.node.key < self.node.right.node.key:
            self.node.right.right_rotate()
            self.left_rotate()
    
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        #insert like normal BST
        if self.node:
            if key < self.node.key:
                if not self.node.left:
                    self.node.left = AVLTree(Node(key))
                else:
                    self.node.left.insert(key)
            else:
                if not self.node.right:
                    self.node.right = AVLTree(Node(key))
                else:
                    self.node.right.insert(key)
        else:
            self.node = Node(key)
        
        # print('root: ', self.node.key)
        # if self.node.left:
        #     print('left child: ', self.node.left.node.key)
        # if self.node.right:
        #     print('right child: ', self.node.right.node.key)
            
        self.update_balance()
        print('balance: ', self.balance)
        
        if self.balance > 1 or self.balance < -1:
            self.rebalance()
            self.update_balance()
            print('balance: ', self.balance)
        
        