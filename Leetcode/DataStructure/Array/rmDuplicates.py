# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        idx = 1
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]:
                nums[idx]=nums[i]
                idx += 1
        return len(nums[:idx])
    

'''
Explain the problem statement.

The problem is to remove duplicates from a sorted array in-palce so that each unique element appears only once. The relative order of the elements should be maintained. We need to return the number of unique elements in the array. After modifying the array, the first part of the array should contain the unique elements, and the rest of the elements are not important.

How did I approach solving this problem?

I approached the problem by using the two-pointer techinique. Since the array is sorted, duplicates will be consecutive. I used one pointer 'idx' to keep track of the position where the next unique element should be placed, and another pointer 'i' to iterate through the array.

The solution runs in linear time, O(n). I'm iterating through the array once with a single loop.
The space complexity is O(1) because I'm not using any extra space that grows with the input size. I'm modifying the array in-place and only using a few extra variables.

I handled edge cases by first checking if the input array is eampty. If it is, the function immediately returns 0. This ensures that we do not encounter errors when accessing elements in an empty array..
'''