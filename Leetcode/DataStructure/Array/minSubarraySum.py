# 209. Minimum Size Subarray Sum

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         # if sum(nums) < target: return 0        
#         # c: the min length
#         # t: the sum of the subarray
#         if sum(nums) < target:
#             return 0

#         m = len(nums)
#         for i in range(len(nums)):
#             t = target
#             for j in range(i, len(nums)):
#                 t = t-nums[j]
#                 if t <= 0:
#                     m = min(m, j-i+1)
#                     continue
#         return m


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        left = 0
        total_sum = 0
        min_length = float('inf')

        for right in range(n):
            total_sum += nums[right]
            print('for right:',right,', total_sum:', total_sum)
            while total_sum >= target:
                min_length = min(min_length, right-left+1)
                total_sum -= nums[left]
                print('total_sum-',nums[left],', left:',left, '-> total_sum=', total_sum)
                left += 1
        return min_length
