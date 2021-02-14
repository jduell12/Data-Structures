"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
- push
- pop

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#array underlying stack structure 
class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, num):
        self.storage.insert(0, num)
        self.size = self.size + 1
        
    def pop(self):
        if self.size == 0:
            return None
        self.size = self.size -1 
        return self.storage.pop(0)

    