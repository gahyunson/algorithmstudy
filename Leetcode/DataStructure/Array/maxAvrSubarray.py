# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''
How to approach?

With 'Sliding Window'.

I attempted to calculate the sum for each sliding window over nums,
but it resulted in a "Time Limit Exceeded" error. We don't need to recaculate the sum for every case.

Fortunately, this problem only asks for the maximum value in a contiguous subraary of length k. 

Time complexity: O(n)
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr = cur_avr = sum(nums[:k])

        for i in range(len(nums)-k):
            cur_avr = cur_avr + nums[i+k] - nums[i]
            if max_avr < cur_avr:
                max_avr = cur_avr
        
        return max_avr/k