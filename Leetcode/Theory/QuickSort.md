# Quick Sort

- Very Fast run time (if already sorted list, be going to sloer runtime)
- Divide and conquer

- 매우 빠르나, 만약 이미 정렬된 것이면 더 느리게 수행된다
- Divide and conquer
- 평균 time complexity : O(nlogn) , 최악 : O(n^2)

1. median -> pivot setting
2. pivot 보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 이동
3. 왼쪽 중 다시 Pivot을 구해서 또 왼족, 오른쪽으로 이동시킴 , 오른쪽도 마찬가지 
4. 더 이상 이동시킬게 없을 때 까지 진행

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] # median
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
```

Leetcode Problem List : 912.