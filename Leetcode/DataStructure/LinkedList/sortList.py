# 148. Sort List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next

        stack.sort()
        newhead = ListNode(0)
        newcur = newhead
        for s in stack:
            newcur.next = ListNode(s)
            newcur = newcur.next
        return newhead.next
            

            