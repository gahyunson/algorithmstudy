# 334. Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i,j,k) such that i<j<k and nums[i]<nums[j]<nums[k]. If no such indices exists, return false.

'''
How to approach?

The goal of this problem is to find three numbers in the array that follow this pattern: the first number should be the smallest, the second number should be greater than the first, and the third number should be greater than the second.

Track two key numbers.
You can set the two numbers less than the last number.

If the current number is smaller than or equal to first, update first to the current number.

If the current number is larger than first but smaller than or equal to second, update second to the current number.

If the current number is larger than both first and second, return True.

If didn't meet the last If, return False.
'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

	'''
	2 have Time Limit Exceeded.

	It was cool idea. but I think the problem is min and max method. 
	It might made the exceeded error.

	'''
    def increasingTriplet2(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(1, len(nums)-1):
            min_num = min(nums[:i])
            max_num = max(nums[i+1:])

            if min_num < nums[i] and nums[i] < max_num:
                return True
            
        return False
