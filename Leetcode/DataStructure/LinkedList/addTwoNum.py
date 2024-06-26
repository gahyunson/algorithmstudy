# 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry = carry // 10
            cur = cur.next
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