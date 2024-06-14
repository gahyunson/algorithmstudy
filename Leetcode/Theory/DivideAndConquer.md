# Divide and Conquer

- 순환적
- 하향식

주어진 문제의 입력을 더 이상 나눌 수 없을 때까지, 
두 개 이상의 작은 문제로 분할,
각 작은 문제 해결,
해들을 결합,
원래 문제의 해를 구함.

알고리즘 종류
- 이진 탐색
- 퀵 정렬
- 합병 정렬
- 선택 정렬

### 이진 탐색
1. 일정한 크기로 2개로 분할, 1개 처리 1개 처리안함
2. 처리한 1개를 2개로 분할, 1개 처리 1개 처리안함
...

### 합병 정렬
1. 일정한 크기로 2개로 분할, 양 쪽다 처리
2. 양 쪽 다 2개로 분할, 양 쪽 다 처리
...

### 퀵 정렬
1. 일정하지 않은 크기로 2개로 분할, 2개 다 처리
2. 일정하지 않은 크기로 2개로 분할, 2개 다 처리
...

### 선택 문제
1. 일정하지 않은 크기로 2개로 분할, 1개만 처리
2. 일정하지 않은 크기로 2개로 분할, 1개만 처리


### 이진 탐색
분할, 정복, ~~결합~~

```
BinarySearch_Iteration(A[], n, x){
    Left=0;
    Right=n-1;
    while(Left <= Right){
        mid = (Left+Right)/2;
        if(x==A[mid]) return mid;
        else if(x < A[mid]) Right = mid-1;
        else Left = mid+1;
    }
}
}
```

input size : n -> 최대 분할 횟수 = n, n/2, n/2^2, ... , n/2^k
-----/-----
--/---
-/-
최대 비교 횟수 = 최대 분할 횟수 + 1

complexity
T(n) = T(n/2) + O(1)
T(n) = O(log n)

### 퀵 정렬
분할, 정복, ~~결합~~    
pivot(분할시 시준이 되는 특정 element, 보통 first element로)이 제자리를 잡도록 하는 정렬 방식    
pivot을 기준으로 왼쪽 부분배열, 오른쪽 부분배열로 나뉜다.

1. 배열의 가장 첫 원소를 pivot으로 지정
2. pivot과 Left 첫번째 원소, Right 마지막 원소와 비교
3. Left < pivot, Right > pivot 인 경우, 해당 위치의 Left, Right값을 서로 바꿔준다
4. 하다가 Left > Right 가 되는 순간, Right, pivot의 위치를 서로 바꿔준다.
5. 왼쪽 부분배열 먼저 진행. 

분할함수 수행 시간 = pivot과 비교 횟수 = O(n)
퀵 정렬 수행 시간 = T(n) = T(Left) + T(Right) + O(n)

최선의 성능인 경우
- pivot을 중심으로 부분배열의 크기가 같은 경우
- pivot이 중앙값인 경우
- T(n)=2T(n/2) + O(n)
- T(n)=O(nlogn)

---/---
-/-----

### 합병 정렬
분할, 정복, 결합
1. 데이터를 나눌 수 없을 때까지 분할
2. 두 가지의 원소 비교, 정렬
3. 합병

분할된 배열 합병하는 방법
- 각 분할된 배열의 가장 첫번째 원소를 각자 비교
- 새로운 배열에 하나씩 넣음

memory complexity = input size
time complexity = T(n) = 2T(n/2) + O(n) = O(nlogn)

```
i=0
j=0
k=0

while(i<n & j<m):
    if(B[i]<=C[j]):
        A[k++]=B[j++]
    else:
        A[k++]=C[j++]
```

### 선택 문제
ex) 정렬되지 않은 배열에서 i번째로 작은 원소를 찾는 문제

1. 오름차순 정렬, i번째 원소 추출
- time complexity : O(nlogn)
- 최악의 경우 : O(n^2)
- 평균의 경우 : O(n)
2. 배열 중 최솟값 찾아 삭제, i번째가 되면 삭제안하고 추출
- time complexity : O(n)을 i번 반복, O(n*i)
- 최악의 경우 : O(n)
- 평균의 경우 : O(n)



```python
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
```

# LeetCode Problems
### 191. Number of 1 Bits

|Runtime                           |Memory                           |
|----------------------------------|---------------------------------|
|35ms                              |17.39MB                          |
|Beats 79.82% of users with Python3|Beats 8.09% of users with Python3|

- Bit = binary scale
- int = decimal
- count '1' in bit == change int to binary and count '1'

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = ""
        while n:
            l = str(n%2)
            n = n//2
            bin_n += l
        
        return bin_n.count('1')

        # print(bin(n))
        # return bin(n)[2:].count('1')
```