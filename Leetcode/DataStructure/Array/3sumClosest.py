from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        numLen = len(nums)
        for i in range(numLen-2):
            left = i + 1
            right = numLen - 1

            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(cur - target) < abs(result - target):
                    result = cur 
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                elif cur == target:
                    return cur 
        return result