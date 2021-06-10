
def bubble_sort(sequence):
    for i in range(len(sequence)-1):
        swapped = False
        for j in range(len(sequence)-1-i):
            if sequence[j] > sequence[j+1]:
                temp = sequence[j]
                sequence[j] = sequence[j+1]
                sequence[j+1] = temp
                swapped = True
            if not swapped:
                break



sequence = [12,45,2,344,55,423,121,3,4556,32,21,12]
bubble_sort(sequence)
print(sequence)