
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data)
        self.head = node
        node.next = self.head


    def print(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            itr = self.head
            while itr:
                print(itr.data)
                itr = itr.next





ll = LinkedList()
ll.insert_at_begining(12)
ll.print()
        