|Name|Worst Case Runtime|Difficulty|   
|---|---|---|
|Bubble sort | n^2 | easiest|   
|Selection sort | n^2 | easier|   
|Merge sort | n*logn | medium|   

# Bubble Sort
- 한 사이클을 돌 때마다 늘 최대값이 가장 마지막 위치로 이동할 것이다.
- 한번 정렬하면 가장 마지막 요소는 최대값으로 고정될 수 있다.
- 그래서 매번 가장 마지막 위치의 인덱스는 더 이상 체크하지 않아도 된다.

- After each cycle, the maximum value will always move to the last position.
- Thus, we can exclude the last index of the array from further checks.
- Continuously reduce the range of the loop index.

```python
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
```


Not working 
```python
def bubblesort(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    for j in range(len(arr)):
        if arr[i] > arr[i+1]:
            bubblesort(arr)
    
    return arr
```

