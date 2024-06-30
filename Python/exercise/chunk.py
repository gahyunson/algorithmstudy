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

'''
The chunk2 function is designed to split a given array into smaller chunckes of a specified size.
'''
def chunk2(array, size):
    # create empty array to hold chunks called 'chunked'
    chunked = []
    
    # For each element in the 'unchunked' array
    for arr in array:
        '''
        chunked=[] , chunked[-1]-> indexerror

        'chunked' is used as reference for 'last'.
        If I use last.append(something), it's going to midify the array inside 'chunked'.
        '''
        # Retrieve the last element in 'chunked'
        last = chunked[len(chunked)-1] if chunked else None
        # if last element doesn't exist, or if its length is equal to chunck size
        if not last or len(last)==size:
            # append a new chunk into 'chunked' with the current element
            chunked.append([arr])
        # else add the current element into the chunk
        else:
            last.append(arr)
    return chunked

print(chunk2([1,2,3,4,5,6,7,8,9],2))
print(chunk2([1,2,3,4,5],3))

# The time Complexity of the function is O(n)
# The space complexity is also O(n) because the function creates a new list that stores all elements of the input array.