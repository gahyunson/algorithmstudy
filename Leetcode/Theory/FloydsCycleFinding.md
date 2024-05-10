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
1. [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, ...] Cycle
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
[Leetcode]()
[reference link](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/)