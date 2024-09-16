# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



class Solution:
    def longestone(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1




    # Runtime: 609ms 5.03%
    # Memory: 17.18MB Beats 14.57%
    def longestOnes2(self, nums: List[int], k: int) -> int:
        con = 0
        idx = 0
        for num in nums:
            if num == 1:
                con += 1
            elif num == 0 and k:
                con += 1
                k -= 1
            else:
                break
            idx += 1
        max_con = con

        while idx < len(nums):
            if nums[idx-con] == 0:
                k += 1
            con -= 1

            while idx < len(nums):
                if nums[idx] == 1:
                    con += 1
                    idx += 1
                elif nums[idx] == 0 and k:
                    con += 1
                    k -= 1
                    idx += 1
                else:
                    break
            
            if max_con < con:
                max_con = con

        return max_con





