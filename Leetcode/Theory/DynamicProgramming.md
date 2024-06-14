# Dynamic Programming
(Divide and Conquer과 상반되는 내용)    
작은 문제의 해를 이용해서 큰 문제의 해를 구할 수 있는 경우 사용하는 알고리즘 
-> 작은 문제의 해를 메모해두고(Memozation) 이용할 수 있다

- ~~상향식, bottom to up 접근 방법~~ Top-Down, Bottom-Up 두 방법이 있음    
~~- Top-Down은 Memozation 이용~~    
~~- Bottom-Up은 tabulation 이용~~

~~- 크기가 작은 문제의 해를 (다시 사용할 수 있으므로)저장, 이를 이용하여 큰 문제의 해를 점진적으로 만들어감~~    
- ~~각 작은 문제는 원래의 문제와 동일, 입력의 크기가 줄어든 것~~    
~~- 작은 문제의 해가 필요할 때마다 바로 사용~~    
- 최적화 문제(max/min)에 사용
- 최적성의 원리 priciple of optimality 를 반드시 만족해야 함

### Kind of DP
- 피보나치 수열
- 연쇄 행렬 곱셈
- 스트링 편집 거리
- 모든 정점의 최단 경로
- 저울 문제

### Memorization
 Top Down
- 큰 문제를 작은 문제로 나눈다
- _작은 문제를 풀어 저장(캐싱)한다 (중복 계산 방지)_
- 작은 문제 해를 이용해 큰 문제를 푼다
- 재귀적 구조
- _Recursive Call_
- caution : check the value's exist in memozation before recursive call

### Tabulation
 Bottom Up
- 크기가 작은 문제부터 차례로 푼다
- 작은 문제부터 풀면 큰 문제는 항상 풀 수 있다
- 모든 문제를 풀 수 있다
- _반복문으로 하위 문제 해결하여 이를 저장_
- _저장된 해를 이용하여 큰 문제를 푼다_

아래 피보나치 수열의 경우 5번째 피보나치 수를 구하는 문제라면,
5개의 변수의 개수만큼 메모하는 배열을 만든다.


### Fibonacci Number 피보나치 수열
if n>=2:
    f(n) = f(n-1)+f(n-2)
elif n==0:
    f(0)=0
elif n==1:
    f(1)=1

So, f(5) = f(4)+f(3) = f(3)+f(2) + f(2)+f(1)     
= f(2)+f(1) + f(1)+f(0) + f(1)+f(0) + f(1)      
= f(1)+f(0)+f(1) + f(1)+f(0) + f(1)+f(0) + f(1)      
= f(1)*5 + f(0)*3      
= 1*5 +0*3 = 5

### 509. Fibonacci Number
- f(0)과 f(1)의 해가 주어진 상태로, Memoization을 이용해서 풀 수 있다. 
- Memoization은 재귀적 구조로 풀 수 있다.

|Runtime                           |Memory                           |
|----------------------------------|---------------------------------|
|337ms                              |17.08MB                          |
|Beats 31.61% of users with Python3|Beats 37.59% of users with Python3|


```python
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)
```

```python
class Test:
    def test(self, n: int) -> bool:
        print(n)
        if n==5:
            return True
        else:
            n+=1
            return self.test(n)
Test().test(0)
```

```python
# Recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n>2:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        
# Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        dp[0]=1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
```

```python
# Recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
# XXXX Time Limit Exceeded XXXX 

# 아래 방법으로 수정하여 사용 가능
# Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
```

```python
# Space Optimization
# 가장 빠른 방법
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
```


### Matrix chain multiplication 연쇄 행렬 곱셈
여러 행렬을 모두 곱셈할 때, 연산을 최소한으로 실행할 수 있는 __곱셈 순서__ 를 찾는 Algorithm!

A = pxq , B = qxr , C = rxs    
(A*B)*C = pxqxr + pxrxs    
A*(B*C) = pxrxs + qxrxs

위 두 연산의 결과는 다르다. 순서에 따라 달라진다 == 더 좋은 방법과 더 안좋은 방법이 있다. => 더 좋은 방법을 찾는것!    
연쇄행렬 최소제곱 알고리즘 점화식을 이용하여 가장 결과 수가 적은 것을 고르면 된다.

```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def dp(i, j):
            m = float('inf')
            for k in range(i+1, j):
                m = min(m, values[i]*values[k]*values[j] + dp(i,k) + dp(k,j))
            
            if m==float('inf'):
                return 0
            return m
        return dp(0, len(values)-1)
```

```python
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def dp(i, j):
            m = float('inf')
            for k in range(i+1, j):
                subproblem_score = values[i]*values[k]*values[j] + dp(i,k) + dp(k,j)
                print(f"dp({i},{j}): subproblem({i},{k}) + subproblem({k},{j}) + {values[i]} * {values[k]} * {values[j]} = {subproblem_score}")
                m = min(m, subproblem_score)
            
            if m==float('inf'):
                return 0
            return m
        
        return dp(0, len(values)-1)

# Example usage:
values = [1, 2, 3, 4, 5]
solution = Solution()
output = solution.minScoreTriangulation(values)
print("Final Minimum Score:", output)
```

### String edit distance/Levenshtein distance 스트링 편집 거리
- Distance between String X and String Y , 두 문자열의 유사도 측정 
- String X에서 String Y로 변환하는 방법에 대한 minimum cost

**Optimality Principle 최적성의 원리**
edit 계산 방법
- insert, delete, replace cost == all '1'


```python
# TEATAO , DADAO 

class Solution:
    def minDistance(self, word1:str, word2:str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0]*(n+1) for _ in range(m + 1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i ==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1],[j-1])
        return dp[m][n]
```

### 모든 정점의 최단 경로
단일 출발점 최단 경로 : 하나의 특정 정점에서 다른 모든 정점으로의 최단 경로    
(데이크스트라 알고리즘 욕심쟁이 방법)

모든 정점 간의 최단 경로 (플로이드 알고리즘)

- 가중치의 합이 음수인 사이클이 존재하지 않는다
- 경유할 수 있는 정점의 범위가 1인 경로부터 시작해서 |V|까지인 경로까지 하나씩 범위를 늘려가면서 모든 정점간의 최단 경로를 한꺼번에 구한다
- 가중치 => 인접 행렬로 표현
- 인접 행렬 




### 저울 문제
**Optility Principle**
- n개의 추로 무게 M인 물체를 확인하는 문제
- 추와 물체의 무게는 정수여야함

1 ~ i번의 추를 이용하여 무게 M을 만들 수 있는가?

