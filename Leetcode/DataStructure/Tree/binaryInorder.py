# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
How to approach?

1. Recursive Method
The recursive approach to an inorder traversal of a binary tree involves visiting the nodes in a specific sequence: first the left child, then the node itself, and finally the right child. 
This process is repeated recursively for each node, continuing until all leaf nodes are reached. The function calls itself recursively until there are no further left or right children to visit, effectively reaching the end of each branch of the tree.

it have to reach leaf node. so i called the function again and again until there is no more left or right node.
'''
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.order(root, result)
        return result

    def order(self, node, result):
        if not node:
            return []
        self.order(node.left, result)
        result.append(node.val)
        self.order(node.right, result)

import unittest

class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        input = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        output = [1,3,2]
        self.assertEqual(solution.inorderTraversal(input), output)

if __name__=='__main__':
    unittest.main()