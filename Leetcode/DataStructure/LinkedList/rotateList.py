# 61. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        # create cycle
        # Set the next of the last element to head
        # 끝까지가서 끝에 head 설정으로 cycle 만들어 주기.
        cur.next = head
        # k값이 늘 나머지 값으로 나오게 해서 
        k = length - (k%length)
        for _ in range(k):
            cur = cur.next
            k -= 1
        
        newhead = cur.next
        cur.next = None 
        return newhead
