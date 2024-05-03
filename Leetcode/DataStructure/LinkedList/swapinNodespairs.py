# 24. Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = head
        cur = dum
        if not head or not head.next:
            return head

        pre = None
        new_list = ListNode(0)
        new_list.next = head
        new_cur = new_list.next
        pair = True
        while cur:
            if pair and cur.next:
                pre = cur.val
                new_cur.val = cur.next.val
                new_cur.next.val = pre
                pair = False
            elif not pair:
                pair = True
            elif not cur.next:
                return new_list.next
        
            cur = cur.next
            new_cur = new_cur.next
        return new_list.next
