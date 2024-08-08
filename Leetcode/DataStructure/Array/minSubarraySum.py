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
'''
e.g. nums=[2,3,1,2,4,3], target=7

2 < 7
2+3 < 7
2+3+1 < 7
2+3+1+2 > 7
min_length = 4

3+1+2 < 7
3+1+2+4 > 7
min_length = 4 -> 4

1+2+4 = 7
min_length = 4 -> 3

2+4 < 7
2+4+3 > 7
min_length = 3 -> 3

4+3 = 7
min_length = 3 -> 2
'''

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
