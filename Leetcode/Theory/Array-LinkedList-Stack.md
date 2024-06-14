# Array And Linked list

### Linked list
head node -> node1 -> node2 -> null

1. insert
1) head node -> node1 -x-> node2 -> null    
node1에서 node2로 향하는 포인트 삭제
2) head node -> node1 -> node1.5 -> node2 -> null    
node1에서 node1.5로 향하는 포인트 추가,    
node1.5에서 node2로 향하는 포인트 추가

2. delete
1) head node -x-> node1 -x-> node2 -> null    
head node에서 node1로 향하는 것과 node1에서 node2로 향하는 포인트 삭제, node1 삭제
2) head node -> node2 -> null    

- 반복문을 이용하여 풀 수 있다.
- 특정 노드 지정안하면 complexity : O(n)
- 특정 노드 지정 complexity : O(1)

어느 위치의 노드를 지정하지 않으면 전체 노드를 돌아야 하기 때문에,    
n개의 node를 봐야해서, **complexity는 O(n)**이 된다.
특정 노드를 지정하면 해당 위치의 노드만 보면돼서 O(1)이 된다.

Random access 불가능, K번째 값을 찾으려면 head부터 포인터를 따라가야한다.

### Array
K번째 새로운 값을 추가/삭제하면, O(N-K) 복잡도가 나온다.

Random access 가능, complexity: O(1)

---
Random access 필요유무에 따라, linked list, array 어떤걸 사용하는게 나을 지 결정할 수 있을 것

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class LinkedList:
    def __init__(self, val):
        self.head = None(val)
    
    def append(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next 
        cur.next = Node(item)
```

# Stack
LIFO (Last In First Out)    
특성 한쪽에서만 insert, delete 연산이 이루어진다 -> 연결리스트로 구현 -> 연산 모두 O(1)이 됨    
연결 리스트 구현 시, head node 부분만 insert, pop 작업이 진행됨     

stack = []

```python
def largestRectangleArea(histogram):
    stack=[]
    max_area=0
    
    for i, h in enumerate(histogram + [0]):
        print("i and h", i, h)
        print("stack",stack)
        while stack and histogram[stack[-1]] > h:
            
            height = histogram[stack.pop()]
            width = i if not stack else i-stack[-1]-1
            print("height and width",height,width)
            max_area = max(max_area, height*width)
            print("max_area",max_area)
        stack.append(i)
        
    return max_area
histogram = [2,1,5,6,2,3]
largestRectangleArea(histogram)
```