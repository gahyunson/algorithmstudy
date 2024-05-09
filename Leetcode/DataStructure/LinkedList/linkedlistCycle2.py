# 142. Linekd List Cycle 2
# Use a Floyd's Cycle-Finding algorithm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

        # if not head or not head.next:
        #     return None
        # stack = []
        # cur = head
        # while cur and cur.next:
        #     stack.append(cur)
        #     if cur.next in stack:
        #         return cur.next
        #     cur = cur.next
        # return None

        # while cur:
        #     if cur not in stack:
        #         stack.append(cur)
        #         cur = cur.next
        #     else:
        #         return cur
        # if not stack:
        #     return None

