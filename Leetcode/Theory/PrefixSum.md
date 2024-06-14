# Prefix Sum

N개의 길이를 가진 배열에서 부분 배열의 합을 구하려고 할때, 
반복문을 이용하면 O(N) 시간이 걸리는데, 이것을 Prefix Sum을 이용해서 O(1)에 구할 수 있다.

내가 보기에 이것은 피보나치 수열 방식과 매우 비슷하다.

total_sum[2]=total_sum[1]+A[1]
total_sum[3]=total_sum[2]+A[2]
이다.

만약 구간 [1,3] 합을 구하고자 한다면,
total_sum[4]-total_sum[1]=A[0]+A[1]+A[2]+A[3]-A[0]
가 된다.

즉, [s,e]구간 값은 total_sum[e+1]-total_sum[s]인 것이다.

total_sum 배열을 처음 선언해줄 때 크기는

N 이 더해야하는 숫자들의 갯수라고 할 때,    
1 ≤ N ≤ 100,000 이라면, total_sum은 100001 크기로 한다.    
왜냐면 100,000번째 값도 더한 값은 100,001번째에 저장해야하기 때문.

```python
A = [1, 4, 6, -3, 0, 2]
pSum = [0,0,0,0,0,0,0]

for i in range(len(A)+1): # range(len(A)+1) = range(7) -> 0,1,2,3,4,5,6 
    pSum[i]=sum(A[:i])
    # [0]
    # [0]+[1]
    # ...
    # [0]+[1]+...+[5]
    # [0]+[1]+...+[5]+[6]
```

```python
def compute_prefix_sum(A):
    N = len(A)
    total_sum = [0] * (N + 1)  # N+1 크기로 total_sum 배열을 초기화
    for i in range(1, N + 1):
        total_sum[i] = total_sum[i-1] + A[i-1]
    return total_sum

def range_sum(total_sum, s, e):
    # [s, e] 구간의 합을 계산
    return total_sum[e+1] - total_sum[s]

# 예제 사용
A = [3, 1, 4, 1, 5, 9, 2, 6]  # 예제 배열
total_sum = compute_prefix_sum(A)
print("Total sum array:", total_sum)

# 구간 [1, 3]의 합을 계산 (1번째부터 3번째 원소까지의 합)
print("Sum of range [1, 3]:", range_sum(total_sum, 1, 3))
```