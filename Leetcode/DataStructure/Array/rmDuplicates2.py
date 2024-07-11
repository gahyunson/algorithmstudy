# 80. Remove Duplicates from Sorted Array II
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    # Check the values two spaces apart.
    # Define new value with new idex.

    # 두 칸 인덱스 간격으로 값을 체크한다. 
    # 새로운 인덱스 값을 이용하여 값을 새로 정의한다.
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        
        idx=2
        for i in range(2, len(nums)):
            if nums[idx-2]!=nums[i]:
                nums[idx]=nums[i]
                idx+=1
        return nums


    # Use a boolean variable to check for duplicates appearing more than twice.
    # If the number has appeared once before, it will be removed on the next occurrence.
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)

        idx = 1
        dup = False
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i] and dup==False:
                nums[idx]=nums[i]
                idx+=1
                dup=True
            elif nums[i-1]==nums[i] and dup==True:
                continue
            elif nums[i-1]!=nums[i]:
                nums[idx]=nums[i]
                idx+=1
                dup = False
        nums = nums[:idx]
        return len(nums)