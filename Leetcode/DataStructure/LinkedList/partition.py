# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 1 4 3 2 5 2
        # 1 2 2
        # 4 3 5
        big = ListNode(0)
        small =  ListNode(0)
        bigcur = big 
        smallcur = small

        while head:
            if head.val < x:
                # print("NO",cur.val)  
                smallcur.next = head
                smallcur = smallcur.next
            else:
                # print(cur.val)  
                bigcur.next = head
                bigcur = bigcur.next
            head = head.next

        # below two codes make difference at runtime. 
        smallcur.next = big.next
        bigcur.next = None

        return small.next
        

            
