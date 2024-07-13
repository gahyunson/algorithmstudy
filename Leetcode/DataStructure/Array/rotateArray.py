# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''
What is the difference between list a and list a[:]?
1. `b = b[:3] + b[3:]`
- create a new list
    that is the concatenation of the first three elements 'b[:3]' and the rest of the elements 'b[3:]'. 
- reassigns this new list to the variable 'b'.
- It doesn't modify the original list in place 
- but rather assigns a new list to the variable 'b'

2. `b[:] = b[:3] + b[3:]`
- modifies the list 'b' in place.
- doesn't create a new list
- but updates the existing list 'b' in place.
'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)

    def rotate2(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

    # Time Limit Exceeded
    # def rotate3(self, nums: List[int], k: int) -> None:
    #     k = k % len(nums)
    #     for _ in range(k):
    #         tmp = [nums[-1]]
    #         nums[:] = tmp + nums[:-1]

import unittest

class Test(unittest.TestCase):
    def test(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]

        solution = Solution() 
        solution.rotate(nums, k)
        self.assertEqual(nums, expected)
    def test2(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]

        solution = Solution() 
        solution.rotate2(nums, k)
        self.assertEqual(nums, expected)

if __name__=='__main__':
    unittest.main()