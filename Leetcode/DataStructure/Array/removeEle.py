# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

'''
How to approach?

It does not matter what you leave beyond the returned k -> 
I don't need to care the values when nums[i]==val. 
Just take the values to front of the array when nums[i]!=val.

Track of two pointers, target elements and non-target elements.
Overwriting the target elements with non-target elements.


'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[idx]=nums[i]
                idx += 1
        return idx
    
