# 437. Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(root, targetSum, cnt):
            # if not root:
            #     return cnt
            if targetSum >= root.val:
                targetSum -= root.val
            if targetSum == 0:
                cnt += 1
                print('cnt:', cnt)
                return cnt
            print(root.val, targetSum, cnt)
            if root.left:
                cnt = dfs(root.left, targetSum, cnt)
            if root.right:
                cnt = dfs(root.right, targetSum, cnt)
            return cnt

        return dfs(root, targetSum, 0)