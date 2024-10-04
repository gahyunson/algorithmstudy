# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                # print(depth)
                return depth
            # print(root)
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        return dfs(root, 0)

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     cnt = 0
    #     left = 0
    #     right = 0

    #     if root.val:
    #         cnt += 1
    #     if root.left:
    #         left = self.check(root.left, cnt+1)
    #     if root.right:
    #         right = self.check(root.right, cnt+1)
    #     return left if left > right else right



    # def check(self, root, cnt):
    #     if root.left:
    #         self.check(root.left, cnt+1)
    #     if root.right:
    #         self.check(root.right, cnt+1)
    #     return cnt


