# 82. Remove Duplicates from Sorted List 2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dum = ListNode(0)
        dum.next = head
        newcur = dum
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur = cur.next
                newcur.next = cur.next
            else:
                newcur = cur
            cur = cur.next
        return dum.next

        # cur = head
        # if not head:
        #     return head

        # newhead = ListNode(0)
        # newhead.next = head
        # newcur = newhead
        # dist_list = []
        # while cur.next:
        #     distinct = None
        #     if cur.val == cur.next.val:
        #         distinct = cur.val
        #         dist_list.append(distinct)
        #     cur = cur.next

        # while head:
        #     if head.val in dist_list:
        #         head = head.next
        #     else:
        #         newcur.next = head
        #         head = head.next
        #         newcur = newcur.next
        # return newhead.next
        