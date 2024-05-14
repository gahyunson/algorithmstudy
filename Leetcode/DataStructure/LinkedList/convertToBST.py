# 109. Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        elif not head.next:
            return TreeNode(head.val)
        
        mid = self.getMid(head)
        tree = TreeNode(mid.val)
        tree.right = self.sortedListToBST(mid.next)
        tree.left = self.sortedListToBST(head)
        return tree
        

    def getMid(self, head):
        slow = head 
        fast = head 
        pre = None

        while fast and fast.next:
            pre = slow
            slow = slow.next 
            fast = fast.next.next 
        if pre:
            pre.next = None 
        return slow 