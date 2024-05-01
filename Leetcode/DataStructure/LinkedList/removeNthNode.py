# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
'''
1. Count the head node's nodes.
2. Then, you can count the number from the front (cnt-n)th.
3. if the node number is the (cnt-n)th, then alternate the .next !
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def cntNodes(self, head: Optional[ListNode]) -> int:
        cur = head
        cnt = 0
        while cur:
            cnt+=1
            cur=cur.next
        return cnt

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = cntNodes(head)
        # print(cnt, n, cnt-n)
        dum = ListNode(0)
        dum.next = head
        recur = dum
        for i in range(cnt+1):            
            if i == (cnt-n):
                recur.next = recur.next.next
                return dum.next
            recur = recur.next
        



            # if cnt < 2 and i == (cnt-n):
            #     print(recur)
            #     print('Here')
            #     # recur.next = ListNode(None)
            #     return recur.next.next
            
            # if cnt >=2 and i == (cnt-n):
            #     print('There')
            #     if recur.next.next:
            #         recur.next = recur.next.next
            #     else:
            #         recur.next = None
            #     return head
            # recur = recur.next

        

