# Floyd's Cycle Finding Algorithm
- A pointer algorithm
- uses only 2 pointers
- using different speeds
- To find a loop in a linked list
- slow pointer, fast pointer
- slow pointer speed x2 = fast pointer speed

- Time complexity : O(n)
- Auxiliary Space : O(1)

### example. 
1. [1, 2, 3, 4, 5, 2, 3, 4, 5, 2 ...] Cycle    
slow = 1 , fast = 1    
slow = 2 , fast = 3    
slow = 3 , fast = 5    
**The fast reach the end**    
slow = 4 , fast = 2    
slow = 5 , fast = 4    
slow = 1 , fast = 1   
**The fast catches the slow**

2. [1, 2, 1] No cycle    
slow = 1 , fast = 1    
slow = 2 , fast = 1    
**The fast reach the end**    

**if** structure is 'head ~ loop starting point ~'

head ~ loop starting point distance ~ the first meeting point ~~~~    
|----- X ----|------------------------- Y -------|    
_____________|------------------------ C -----------------------|    
loop starting point ~ the first meeting point = Y    
1 loop distance = C    

--- 
Can make formulars ...
1. slow = X + Y + C*s    
2. fast = X + Y + C*f

slow speed * 2 = fast speed , two points have meeting point so,
- slow * 2 = fast

Thus,

2(X+Y+Cs) = X+Y+Cf    

X+Y = Cf - 2Cs = (f-2s)C = K*C (K is some positive constant)

X = KC - Y

so, I can prove 'why reseted slow to head is always working?'

1. slow location = X + Y
    fast location = X + Y
2. slow reset to head
3. 
    a) slow location = X    
    b) fast location = X + Y + X   
        X = X + Y + X   
        X = X + Y + (KC - Y) = X + KC

C is one time loop, it starts on X.

KC - Y 에서 Y만큼 왔던 Y distance 를 해결하면, loop start point ~ loop end point 한 횟수를 C 만큼 움직이는 거니까, 
slow 가 출발지점 X 만큼 온 것돠 C 루프를 반복하는 출발점에 있는 것이 같다.

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def detectLoop(head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # The fast catches the slow
            if slow == fast:
                return 'Loop exists in the Linked List'
        # The fast reach the end
        return 'Loop doesn't exist in the Linked List'
```

**If** you have to know the meeting point
- Time complexity : O(n)
- Auxiliary space : O(1)
```
def detectLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow==fast:
            break
    if slow!=fast:
        return None
    
    # initially slow. and then we can find a meething point
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow
```

Leetcode Problem List : 141. Linked List Cycle, 142. Linked List Cycle 2    
[reference link](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/)