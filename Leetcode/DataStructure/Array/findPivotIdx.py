# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        How to approach?

        If left == right, then: right - the left == 0.
        I didn't store the values of the left, I decreased the right values immediately.

        Complexity
        - Time complexity:
        $$O(n)$$

        - Space complexity:
        $$O(1)$$
        '''
        pre = sum(nums[1:])

        if pre == 0:
            return 0
        i = 0
        while i < len(nums)-1 :
            pre -= (nums[i]+nums[i+1])
            if pre == 0:
                return i+1
            i += 1
        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        """
        Runtime 8ms Beats 42.19%
        Memory 18.11MB Beats 10.68%
        """
        idx = 0

        lt_sum = 0
        rt_sum = sum(nums[1:])

        if rt_sum == 0:
            return 0

        while idx+1 < len(nums):
            if lt_sum != rt_sum:
                lt_sum += nums[idx]
                idx += 1
                rt_sum -= nums[idx]
            else:
                return idx
        if lt_sum == rt_sum:
            return idx
        return -1

