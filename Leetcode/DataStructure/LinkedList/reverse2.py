# 92. Reverse Linked List 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        

        newhead = ListNode(0)
        newcur = newhead
        new = None
        cnt = 1
        while head:
            if cnt == left:
                while cnt <= right:
                    cnt += 1
                    tmp = head.next
                    head.next = new
                    new = head
                    head = tmp
                newcur.next = new
                while newcur.next:
                    newcur = newcur.next
            else:
                cnt += 1
                newcur.next = head
                head = head.next
                newcur = newcur.next

        return newhead.next