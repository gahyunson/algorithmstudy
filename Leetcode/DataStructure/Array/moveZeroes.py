# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    '''
    How to appraoch?

    (I accepted that sliding is inefficient)
    I was using the two point for index.
    
    1. Pointer 'i': to check if the element of 'nums' is non-zero
    2. Pointer 'idx': tracks the position and reassign

    if the element is not 0 (nums[i]), assign it to nums[idx].
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        idx = 0

        while i < len(nums):
            if nums[i]!=0:
                nums[idx] = nums[i]
                idx += 1
            i += 1
        
        for i in range(idx, len(nums)):
            nums[i] = 0


    '''
    How to approach?

    I reassign elements by shifting them when the element is non-zero.
    For example: [0, 1, 1] -> [1, 1] -> [1, 1, 0]

    However, I couldn't properly imcrement the index 'i' when encountering a zero.
    But in the end, the zero is always placed at the last position of the array.    
    '''
    # Output Limit Exceeded
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            print(nums, nums[i])
            if nums[i] == 0:
                nums[i:] = nums[i+1:]
                nums.append(0)
            else:
                i += 1
        