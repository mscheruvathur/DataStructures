
def selection_short(sequence):
    size = len(sequence)
    for i in range(len(sequence)-1):
        min_index = i
        for j in range(min_index+1,len(sequence)):
            if sequence[j] < sequence[min_index]:
                min_index = j
            
        if i != min_index:
            sequence[i],sequence[min_index] = sequence[min_index],sequence[i]


sequence = [12,45,2,344,55,423,121,3,4556,32,21,12]
selection_short(sequence)
print(sequence)