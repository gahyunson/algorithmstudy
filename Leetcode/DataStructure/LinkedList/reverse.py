# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
How to approach?

1 -> 2 -> 3 -> 4 -> 5

1 -> None , 2 -> 3 -> 4 -> 5
2 -> 1 -> None , 3 -> 4 -> 5
3 -> 2 -> 1 -> None , 4 -> 5
4 -> 3 -> 2 -> 1 -> None , 5
5 -> 4 -> 3 -> 2 -> 1 -> None

Time complexity: O(n)
Space complexity: O(1)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            daum = head.next
            head.next = pre
            pre = head
            head = daum
        return pre