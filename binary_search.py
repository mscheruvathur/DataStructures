
index = 0
def binary_search(sequence,item):
    begining_index = 0
    end_index = len(sequence) -1
    mid_index = 0

    while begining_index <= end_index:
        mid_index = (begining_index + end_index) // 2
        mid_number = sequence[mid_index]

        if mid_number == item:
            globals()['index'] = mid_index
            return True
        elif mid_number < item:
            begining_index = mid_index + 1
        else:
            end_index = mid_index - 1
    
    return False


sequence = [1,2,3,4,5,6,7,8,9,10]
item = 10

if binary_search(sequence,item):
    print(f'item founded at index {index} using binry search')
else:
    print('sorry the item not founded')


