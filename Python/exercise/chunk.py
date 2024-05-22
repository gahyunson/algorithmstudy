# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

# for loop , index slice
def chunk1(array, size):
    result = []
    for i in range(len(array)//size+1):
        result.append(array[i*size:(i+1)*size])
    return result

# while loop , index slice
def chunk3(array, size):
    chunked = []
    index = 0
    while (index< len(array)):
        chunked.append(array[index:index+size])
        index = index + size
    return chunked

def chunk2(array, size):
    chunked = []
    
    for arr in array:
        '''
        chunked=[] , chunked[-1]-> indexerror

        'chunked' is used as reference for 'last'.
        If I use last.append(something), it's going to midify the array inside 'chunked'.
        '''
        last = chunked[len(chunked)-1] if chunked else None
        if not last or len(last)==size:
            chunked.append([arr])
        else:
            last.append(arr)
    return chunked

print(chunk2([1,2,3,4,5,6,7,8,9],2))
print(chunk2([1,2,3,4,5],3))