# 1493. Longest Subarray of 1's After Deleting One Element
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1

        i = 0
        k = 1
        max_len = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            if max_len < (j - i):
                max_len = (j-i)
        return max_len
            

        # max_arr = 0

        # cnt = 0
        # k = 1
        # j = i = 0
        # while i < len(nums):
        #     if nums[i] == 0 and k==1:
        #         k -= 1
        #         i += 1
        #     elif nums[i] == 0:
        #         if max_arr < cnt:
        #             max_arr = cnt
        #         cnt = 0
        #         k += 1
        #         j += 1
        #         i = j
        #     elif nums[i] == 1:
        #         cnt += 1
        #         i += 1

        # if max_arr < cnt:
        #     max_arr = cnt
        # return max_arr