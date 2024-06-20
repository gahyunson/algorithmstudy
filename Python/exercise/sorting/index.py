# --- Directions
# Implement bubbleSort, selectionSort, and mergeSort

# O(n^2)
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# Recursive 
# Worst time complexity : O(n^3) or infinite ...
def bubblesort2(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    for j in range(len(arr) - 1):
        print(arr)
        if arr[j] > arr[j+1]:
            bubblesort(arr)

    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        indexOfMin = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[indexOfMin]:
                indexOfMin = j
        
        if indexOfMin != i:
            arr[indexOfMin], arr[i] = arr[i], arr[indexOfMin]

    return arr

# contain recursive code
def mergeSort(arr):
    if len(arr)==1:
        return arr 
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    return merge(mergeSort(left), mergeSort(right))

# doesn't contain any recursive code
def merge(left, right):
    # return left + right sorted
    results = []
    while left and right:
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    results.extend(left)
    results.extend(right)
    return results 