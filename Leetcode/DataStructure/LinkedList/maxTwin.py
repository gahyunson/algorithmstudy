# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

'''
Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        ant = 0
        post = len(arr)-1
        num = 0
        while ant < post:
            if num < arr[ant] + arr[post]:
                num = arr[ant] + arr[post]
            ant += 1
            post -= 1
        return num

    '''Time Limit Exceeded'''
    def pairSum2(self, head: Optional[ListNode]) -> int:
        curr = head
        total = []
        while curr:
            total.append(curr.val)
            curr = curr.next

        curr = head
        nxxt = None
        cnt = 0
        while curr:
            cnt += 1
            tmp = curr.next
            curr.next = nxxt
            nxxt = curr
            curr = tmp

        for i in range(cnt//2):
            total[i] = total[i] + nxxt.val
            nxxt = nxxt.next

        return max(total[:cnt//2])