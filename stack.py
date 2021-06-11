from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def append(self,val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def print(self):
        print(self.stack)

st = Stack()
