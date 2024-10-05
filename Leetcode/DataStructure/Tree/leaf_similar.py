# 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

'''
How to approach? DFS

Keep calling the function recursively until the node is None.
A leaf doesn't have any children node under its left and right,
so I can identify it when not root.left and not root.right.
In this case,I add the leaf value to an array.

Time complexity: O(n+m)
Space complexity: O(n+m)
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, arr):
            if not root.left and not root.right:
                arr.append(root.val)
                print('not',arr)
                return arr
            if root.left:
                print('left',arr)
                dfs(root.left, arr)
            if root.right:
                print('right',arr)
                dfs(root.right, arr)
            return arr
        return dfs(root1, []) == dfs(root2, [])