# 817. Linked List Components
# Definition for singly-linked list.
'''
Matching pairs using a boolean flag!!!
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        cnt = 0
        in_component = False
        while head:
            print(head.val)
            if head.val in nums_set:
                if not in_component:
                    cnt += 1
                    in_component = True
            else:
                in_component = False
            head = head.next
        return cnt