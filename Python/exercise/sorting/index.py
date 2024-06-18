# --- Directions
# Implement bubbleSort, selectionSort, and mergeSort


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr



''' # Not working
def bubblesort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    for j in range(len(arr) - 1):
        print(arr)
        if arr[i] > arr[i+1]:
            bubblesort(arr)
    # [-40, 100, -124, 0, 21, 7, 500]
    return arr
'''
