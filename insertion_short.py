

def insertion_short(sequence):
    for i in range(1,len(sequence)):
        anchor = sequence[i]
        j = i - 1
        while j >=0 and anchor <= sequence[j]:
            sequence[j+1] = sequence[j]
            j = j - 1
            sequence[j+1] = anchor


sequence = [12,45,2,344,55,423,121,3,4556,32,21,12]
insertion_short(sequence)
print(sequence)