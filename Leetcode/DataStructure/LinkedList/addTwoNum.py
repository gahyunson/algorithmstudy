# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

'''
How to approach?

Add the values of 'l1' and 'l2' nodes sequentially, 
directly putting the sum into the corresponding linked list node.
To maintain the digit in the units place, if the sum is 10 or greater, add 1 to the next value.

l1과 l2 값들을 차례대로 각자 더해준 값을 바로 링크노드 값에 넣어준다.
일의 자리 형태를 유지하기 위해서 10이상의 경우 그 다음 값에 1을 더해준다.
'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialization
        # create a dummy node to store the result list.
        dum = cur = ListNode(0) # use a pointer 'cur' to traverse
        carry = 0 # initialize a variable 'carry' to handle carry-over

        # Addition Process
        while l1 or l2 or carry:
            # At each step, we add the values from 'l1' and 'l2' nodes
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            # create a new node in the result list
            cur.next = ListNode(carry%10)
            carry = carry // 10 # update the carry divided by 10, for the next higher place value
            cur = cur.next # move the cur pointer to the next node
        # and return the next node of the dummy node
        return dum.next
    
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""
        while l1:
            num1 = num1+str(l1.val)
            l1=l1.next
        while l2:
            num2 = num2+str(l2.val)
            l2=l2.next
        num1, num2=num1[::-1], num2[::-1]        
        result = int(num1)+int(num2)
        
        res_node = ListNode(0)
        nodes = res_node
        print(res_node)

        for r in str(result)[::-1]:
            nodes.next = ListNode(r)
            nodes = nodes.next
        return res_node.next