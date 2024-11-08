# # Day 10. (Sep 21)
# ### 283. Move Zeroes
# Move all 0's to the end of an array nums. The first code is my solution, and the second one is someone else's solution on LeetCode.

# I want to move the indices of 0 values to the end of the array. In my initial solution, I remove a 0 value and add it to the end. However, this solution has a runtime of 781 ms. I believe the reason for this is that I perform calculations twice within a for loop. I think I can reduce the runtime by minimizing the calculations.

# There is an alternative solution: if a value is not 0, initialize the array with that value, and if the value is 0, skip it. In the last step, append a 0 value to the array to account for the remaining length.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
            else:
                pass"""

        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1

