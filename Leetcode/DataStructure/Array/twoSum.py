# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

'''
How to approach?

"target" is sum of two numbers from the 'nums' array. Therefore, one of the numbers can be found by subtracting another number in the array from the target, So, if 'target-nums[i]' exists in the 'nums' array, we have found a pair that adds up to the target.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
            
