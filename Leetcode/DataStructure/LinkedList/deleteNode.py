# 237. Delete Node in a Linked List
# Definition for singly-linked list.
'''
You are given the node to be deleted node. You will not be given access to the first node of head.
-> have to use only ‘node’

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list. 
-> always have .next
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        