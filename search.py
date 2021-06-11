

class Search:

    def __init__(self):
        self.sequence = None

    def insert_value(self,sequence):
        self.sequence = sequence

    def binary_search(self,item):
        index = 0
        begining_index = 0
        end_index = len(self.sequence) -1
        mid_index = 0

        while begining_index <= end_index:
            mid_index = (begining_index + end_index) // 2
            mid_number = self.sequence[mid_index]

            if mid_number == item:
                index = mid_index
                print(f'item founded at index {index} using binry search')
                return
            elif mid_number < item:
                begining_index = mid_index + 1
            else:
                end_index = mid_index - 1
        
        print('sorry the item not founded')


    
    def linear_search(self,item):
        index = 0
        for i in range(1,len(self.sequence)+1):
            if i  == item:
                index += i-1
                print(f'item founded at index {index} using linear search')
                return
        print('sorry the item not founded')



    


sequence = [1,2,3,4,5,6,7,8,9,10]        
se = Search()
se.insert_value(sequence)
se.linear_search(20)
