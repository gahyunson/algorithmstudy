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
        
        '''
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            # fast = fast.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head) # 4 2
        right = self.sortList(mid) # 1 3

        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                # print("if",left.val, right.val)
                curr.next = left
                left = left.next
            else:
                # print("else",left.val, right.val)
                curr.next = right
                right = right.next
            # print("curr",curr)
            curr = curr.next
        # print("exit")
        print('cr',curr)
        print('left',left, 'right',right)
        curr.next = left or right
        print(curr)
        # print("dummy",dummy)
        return dummy.next
        '''

            