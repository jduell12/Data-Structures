"""
Max Heap

Root node is the greatest among all the nodes. The property is true for all sub trees in the heap
"""
class Heap:
    def __init__(self):
        self.storage = []
        self.length = 0
        
    #gets the index of the parent node
    def parent(self, index):
        return index//2

    def insert(self, value):
        #checks if heap is empty
        if self.length == 0:
            self.storage.append(value)
            self.length += 1
        else:
            #insert element into array
            self.storage[self.length] = value  
            self.length += 1
            #check through array to make sure it is ordered correctly
            current = self.length 
            # while self.storage[current] > self.storage

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
