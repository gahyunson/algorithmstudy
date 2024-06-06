# hungarian algorithm
전체 비용을 최소화하는 할당을 찾는다.

법칙
- 최적의 할당 찾기
- 행렬로 이루어져야 한다

2. 알고리즘 개념
- 행렬 구조: 각 행은 노동자를, 각 열은 작업을 나타내며, 행렬의 각 요소는 해당 노동자가 해당 작업을 수행하는 비용을 의미
- 최소화 원리: 각 행 또는 열에서 최솟값을 찾아 전체 행렬에서 그 값을 빼서, 각 행에 최소 하나의 0이 포함되도록 만든다.

1. row 혹은 col 중 최솟값을 골라, 해당 row , col 에 빼준다. 어차피 해당 행을 처리하는데 1씩 cost가 들기 때문에 ㄱㅊ다.

2. 모든 행에는 0이 있도록 위 작업을 계속한다.

3. 각 행과 열에서 0 위치를 고른다.인덱스가 중복되면 안된다.
4. 해당 위치의 원래 데이터에서 해당 위치의 데이터 값들을 합친다.

scipy.optimize 모듈 linear_sum_assignment

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
row_ind, col_ind = linear_sum_assignment(cost)
optimal_cost = cost[row_ind, col_ind].sum()

print("Optimal assignment:", list(zip(row_ind, col_ind)))
print("Minimum cost:", optimal_cost)
```