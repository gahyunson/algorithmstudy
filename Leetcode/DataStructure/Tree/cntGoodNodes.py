# 1448. Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS.
        I manage the maximum value by storing a pair of current root info.

        Time complexity: O(n)
        Space complexity: O(logn) - O(n)
        """
        if not root:
            return 0

        stack = [(root, -10**4)]
        good = 0
        while stack:
            r, m = stack.pop()
            if r.val >= m:
                good += 1
                m = r.val

            if r.left:
                stack.append((r.left, m))
            if r.right:
                stack.append((r.right, m))
        return good

    def goodNodes2(self, root: TreeNode) -> int:
        """
        Runtime Error
        IndentationError: unindent does not match any outer indentation level
        """
        def dfs(root, arr):
            if not root:
                return []
            if root.val >= arr[-1]:
                arr.append(root.val)
            print(root.val, arr)
            dfs(root.left, arr)
            dfs(root.right, arr)
            return arr
        result =  dfs(root, [-10**4])
        print(result[1:])
        return len(result)-1

