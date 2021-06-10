
index = 0
def linear_search(sequence,item):
    for i in range(1,len(sequence)+1):
        if i  == item:
            globals()['index'] += i-1
            return True
    return False


sequence = [1,2,3,4,5,6,7,8,9,10]
item = 2

if linear_search(sequence,item):
    print(f'item founded at index {index} using linear search')
else:
    print('sorry the item not founded')