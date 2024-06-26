# Sparse Table 

- O(n logn)
- arrow graph
- To find the minumum or maximum value in a particular range of an array
- building up from smaller ranges to larger ones

- 1 위치에서 5번째 앞에 위치한 정점 찾는 방법
- 1에서 5번째를 세알려서 이동하여 정점을 찾는다 - O(n)

- 5 = 101(2) = 2^0 + 2^2 = 1 + 4 , 1번 정점에서 1번째 앞에 위치한 정점 = 2 ~ 2번째 정점에서 4번째 앞에 위치한 정점 = 6 => 1 정점에서 5번째 앞에 위치한 정점 = 6

```python
import math

def build_sparse_table(arr):
    n = len(arr)
    k = math.floor(math.log2(n)) + 1 # 2진법
    st = [[0] * k for _ in range(n)]
    
    # 초기 구간 길이 1에 대한 처리
    for i in range(n):
        st[i][0] = arr[i]
    
    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
            i += 1
        j += 1
    print(st)
    return st

def query(st, L, R):
    j = math.floor(math.log2(R - L + 1))
    return min(st[L][j], st[R - (1 << j) + 1][j])

# 예시 사용
arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
st = build_sparse_table(arr)
print(query(st, 0, 4))  # 0 출력
print(query(st, 4, 7))  # 3 출력
print(query(st, 3, 3))  # 0 출력
```