# 203. Remove Linked List Elements
# Definition for singly-linked list.
'''
result = ListNode(0)
test = head
result.next = head
cur = result
print(cur is head, cur == head, test is head, test == head) head와 연관되지 않게 새로운 result 변수를 만든것이다.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        full_res = ListNode(0)
        full_res.next = head
        cur = full_res

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                # print('in here')
            else:
                cur = cur.next
        return full_res.next

        # result = ListNode(0)
        # cur = result

        # while head:
        #     print(head.val, val)
        #     if head.val == val:
        #         print('I got it')
        #         head = head.next
        #         print(cur)
        #     else:
        #         print('Dont mind')
        #         cur.next = head
        #         cur = cur.next
        #         head = head.next
        #         print(cur)
            
        
        # return result.next



        



