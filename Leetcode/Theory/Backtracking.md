그래프, 트리를 탐색하는 알고리즘
DFS, BFS -> 모든 노드를 탐색하는 방법
Backtracking -> 가능한 해를 탐색

# Backtracking
- 가능한 모든 조합 시도,
- 시도 중 해결책이 아니면 중단하고 이전 단계로 돌아가서 다음 조합 시도.
- 모든 경우의 수 중 특정 조건을 만족하는 해를 찾아야하는 경우 사용

트리의 경우 DFS로 진행하고 해당 조합이 알맞지 않다면 DFS값을 초기화하고 다음 조합의 해를 확인하는 식으로 진행