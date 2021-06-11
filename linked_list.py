


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    
    def insert_new_value(self,data):
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

    def remove_by_value(self, data):
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


    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.head == self.head.next
            return
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def remove_from_end(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None
    

        
    
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self,value,data):
        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
        

    def insert_before_value(self,value,data):
        if self.head is None:
            return
        itr = self.head
        while itr:

            if itr.data == value:
                self.insert_at_begining(data)
                break
            elif itr.next.data == value:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next


    def remove_duplicates(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            itr = itr.next
        

        

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ','
            itr = itr.next
        print(llstr)


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

    
    


ll = LinkedList()
values = ['sam','abhi','sanu','salva']
ll.insert_new_value(values)
ll.print()
ll.insert_before_value('abhi',12)
ll.insert_after_value('abhi',12)
ll.insert_before_value('sam',12)
ll.insert_before_value(12,'newone')
ll.insert_before_value('salva',12)
ll.insert_before_value('salva',33)
ll.print()
