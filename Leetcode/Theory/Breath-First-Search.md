# Depth-fist search DFS 깊이 우선 탐색


# Breadth-first search BFS 너비 우선 탐색    
모든 정점을 하나씩 순회하기 위한 방법    

1. component의 갯수
2. component의 크기
를 구하기 위해 사용 가능

DFS와 다르게 같은 레벨의 노드들을 파는 위주로 진행

example)
0
1 _ 2 _
3 4 5 6

위와 같은 노드에서 DFS의 경우,    
0 - 1 - 3 - 4 - (1 - 0 ) - 2 - 5- 6    
순으로 진행되고,     
BFS의 경우,    
0 - 1 - 2 - 3 - 4 - 5 - 6    
순으로 진행됨.

[leetcode Same Tree BFS 문제](https://leetcode.com/problems/same-tree/)
- p에는 Treenode 구조로 데이터가 들어가 있음
- val, left(val, left, right), right(val, left, right)
- 여기서 val 내용만 나열된 리스트가 필요함
- val, val, val, val, left, right 이런식으로 고쳐줘야함
- 여기서 val로 모두 값을 바꾸는 순서는 ... 인덱스 0 자리부터 시작해서 나열.

- left2, right2, left3, right3 순서대로 만들기
- left와 right값만 현재 데이터를 뽑아서 정제중인 변수인 queue의 맨끝에 계속 추가해서 작업이 가능하도록, val의 뒤에 위치하도록 해서 각 노드의 레벨의 위치에 맞게 설정해준다.
- result에는 val값만 계속추가해준다.

- node의 값이 없는 경우, val.left.right속성없이 None으로 저장되어있으므로, if절을 이용해 None값을 처리해준다.

(처음 생각한 방법)
for문을 이용하여 n번째 인덱스까지 끊어서 바로 비교한다 -> val, left, right 때문에 불가능?

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p)==self.bfs(q)
        
    def bfs(self, p: Optional[TreeNode]) -> list:
        result = []
        print("p:",p)
        queue = [p]
        print("queue:",queue)
        while queue:
            elem = queue.pop(0)
            print("elem:",elem)
            if elem == None:
                result.append(None)
                continue
            result.append(elem.val)
            queue.extend([elem.left, elem.right])
        print("result:",result)
        return result
```

# 101. Symmetric Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.bfs_left(root)==self.bfs_right(root)
        
    def bfs_left(self, root: Optional[TreeNode]) -> list:
        start = root.val
        left_node = root.left
        left_node = [left_node]

        left_list = []
        while left_node:
            node = left_node.pop(0)
            # print(node.val)
            if node==None:
                left_list.append(None)
                continue
            left_list.append(node.val)
            left_node.extend([node.left, node.right])

        return left_list

    def bfs_right(self, root: Optional[TreeNode]) -> list:
        start = root.val
        right_node = root.right
        right_node = [right_node]

        right_list = []
        while right_node:
            node = right_node.pop(0)
            # print(node.val)
            if node==None:
                right_list.append(None)
                continue
            right_list.append(node.val)
            right_node.extend([node.right, node.left])

        return right_list
```