# 21. Merge Two Sorted Lists

'''
Time complexity : O(n+m) 
Space complexity : O(1)

How to approach?

I create a dummy ListNode to which I will attach elements from the lists.
I select the smaller values from the lists in sequence and attach them to the new list.

새로운 리스트 노드 변수를 만들어서 
list1, list2 값을 차례대로 비교하여
작은 값부터 순서대로 넣어주었다.
'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution21:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next 

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next
    
'''list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution21()
merged_head = solution.mergeTwoLists(list1, list2)

def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

print_list(merged_head)'''