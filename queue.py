from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def print(self):
        print(self.queue)


que = Queue()
que.enqueue(12)
que.enqueue(13)
que.enqueue(14)
que.print()
que.dequeue()
que.print()

    