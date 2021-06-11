
class Node:
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data)
            node.prev = None
            self.head = node
        else:
            node = Node(data)
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
            node.prev = itr
            node.next = None


    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data)
            node.prev = None
            self.head = node
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev = None

    def insert_after_value(self,value,data):
        pass

    def insert_before_value(self,value,data):
        pass
    
    def  insert_new_value(self,data):
        self.head = None
        for data in data:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    
    
    def print_by_order(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        dllst = ''
        while itr:
            dllst += str(itr.data) + ','
            itr = itr.next
        print(dllst)
    
    def print_by_reverce(self):
        if self.head is None:
            print('Linked list is empty')
        prev = None
        itr = self.head
        dllst = ''
        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        self.head = prev
        itr = self.head
        while itr:
            dllst += str(itr.data) + ','
            itr = itr.next
        print(dllst)
        
        



dl = DoublyLinkedList()
lst= [12,34,45,56,67,7,78,]
dl.insert_new_value(lst)
dl.insert_at_end(444)
dl.insert_after_value(34,333)
dl.print_by_order()