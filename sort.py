

class Sort:

    def __init__(self):
        self.array = None
    
    def isnert_value(self,sequence):
        self.array = sequence

    def print(self):
        print(self.array)
    
    def bubble_sort(self):
        for i in range(len(self.array)-1):
            swapped = False
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp
                    swapped = True
            if not swapped:
                break
    

    def insertion_short(self):
        for i in range(1,len(self.array)):
            anchor = self.array[i]
            j = i - 1
            while j >=0 and anchor <= self.array[j]:
                self.array[j+1] = self.array[j]
                j = j - 1
                self.array[j+1] = anchor

    

    def selection_short(self):
        
        size = len(self.array)
        for i in range(len(self.array)-1):
            min_index = i
            for j in range(min_index+1,len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
                
            if i != min_index:
                self.array[i],self.array[min_index] = self.array[min_index],self.array[i]
    

        







        

sequence = [12,45,2,344,55,423,121,3,4556,32,21,12]

arr = Sort()
arr.isnert_value(sequence)
arr.print()
arr.bubble_sort()
arr.print()
