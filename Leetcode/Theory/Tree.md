Graph and... Tree!
1. 연결 그래프이다. 컴포넌트가 하나이다. 
2. 싸이클이 존재하지 않는다.
3. 트리의 간선 개수 = 트리의 정점 개수 - 1


싸이클은 없지만 모든 노드는 연결되어있다.

차수 : 자신 바로 아래레벨에 연결된 노드 갯수
차수가 3이라면 3진트리

Sub Tree : Tree 속의 부분 Tree
트리의 자식이 트리.... -> 재귀적 성질 

Graph를 순회하는 방법 
1. DFS
2. BFS

Tree를 순회하는 방법
1. preorder traversal 전위 순회
    root, left, right
2. inorder traversal 중위 순회
    left, root, right
3. postorder traversal 후위 순회
    left, right, root
4. levelorder traversal 레벨 순회
5. ...

![image.png](attachment:image.png)


```python
children = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    5: [7],
    6: None
    
}
if 0 in children:
    print("okay")
if 3 in children[0]:
    print("3 okay")
if 3 in children:
    print("3 33")
if children[6]:
    print(666)
print(children.keys, children.values)
```

```python
# 재귀함수 사용하는 방법
def get_height(root, children):
    print("original root is",root, "and children is",children)

    # root로 설정한 값이 dict key값에 있거나, 아니면 해당 root가 자식노드가 있는지?
    if root not in children or not children[root]:
        print("not in")
        print("-"*60)
        return 1
    
    result=1
    for c in children[root]:
        print("c is",c)
        result=max(result, get_height(c, children)+1) # +1 하는 이유는 한 level당 1개 높이를 추가해서 총 높이를 확인하는 방법 
        print("temp result is",result,"*"*10)
        
    print("*"*20)
    print("result root is",root, "and children is",children)
    return result
children = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    5: [7]
    
}

height = get_height(0, children)
print(f"The height of the tree is: {height}")
```

```python
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)
```

val=0, left=(val==1, left=(val=... left=(val=0, left=None, right=None)), right = 

# Binary Tree

Root    
Left, Right    
: Left < Root > Right

- Perfect binary tree 
- Complete binary tree

N개의 정점의 트리
- O(logN)
- worst : O(N)

- balanced tree 를 이용하여 worst에서 벗어나게 할 수 있음

### Binary tree insert
root에서부터 크기 비교하면서 Letf , Right 어디에 위치시킬 건지 보면 됨

### delete
1. leaf node의 경우
해당 leaf node만 delete

2. 자식 노드가 하나 있는 경우
자식 노드와 부모 노드를 이어준다.

3. 자식 노드가 둘 있는 경우
해당 노드의 자식 노드 둘 중 아무거나가 해당 노드의 자리로 올라간다.
둘 중 아무거나란? 왼쪽과 오른쪽에서 하나씩 고르는데, 
왼쪽은 해당 노드와 가장 가깝게 작아야하고,
오른쪽은 해당 노드와 가장 가깝게 더 커야한다.