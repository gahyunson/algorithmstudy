# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        destination = size-1

        cur_coverage, last_jump_index = 0, 0
        total_jump = 0

        if size == 1:
            return 0
        
        for i in range(0, size):
            cur_coverage = max(cur_coverage, i+nums[i])
            if i == last_jump_index:
                last_jump_index = cur_coverage
                total_jump += 1
                if cur_coverage >= destination:
                    return total_jump
        return total_jump

        # idx = len(nums)-2
        # cnt = 0
        # for i in range(len(nums)-2, 0, -1):
        #     if i+nums[i] >= len(nums)-1:
        #         # idx = min(i, idx)
        #         if idx > i:
        #             print(i, len(nums), nums[i], i+nums[i], idx, cnt)
        #             idx = i
        #             cnt += 1
