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

