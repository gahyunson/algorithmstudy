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

'''
Example: [2,3,1,1,4]

We can transform the array [2,3,1,1,4] to [2,4,3,4,8].   

It can 2 steps from 0 index.
It can 4 steps from 0 index.
It can 3 steps from 0 index.
It can 4 steps from 0 index.

what you can observe with [2,4,3,4,8] is that   
you can evaluate each element without having to count each index individually.
--you can check the element without counting each index.--

Check all elements from index 0 to the last index.
(You might be able to return before reaching the end! If it determined that the last index is reachable)

1. The greater value can reach the last index.
farthest: 2 -> 3 

2. `farthest >= len(nums)-1`
If farthest == 3 , then len(nums)-1 = 4 
    3 >= 4 => It reached!

3. `i==end`
The point is each range.
You define the maximum number within the range from 0 to end as farthest.   
You will select the number within the range, you can count it as 1 jump.
Next, You will reach the last index of the array or select again the max number then, end define the max number plus 1 to jump.

0~end 범위 안에서 가장 큰 값을 다음 end로 지정하기 위해 farthest 를 정의한다. 
아무튼 end 범위 안에서 하나의 숫자를 선택했으므로 1 jump를 한 것으로 간주하고,
그 다음 end 범위 안에서 마지막 인덱스에 도착하던가 아니면 또 다시 가장 큰값을 고르고 그 다음 end값으로 지정하여 2 jump 한 것으로 계산된다.

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums)-1:
                cnt += 1
                return cnt
            if i==end:
                cnt += 1
                end = farthest
        return cnt

class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            print('keep increase:', farthest)
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums)-1:
                print('End', farthest)
                cnt += 1
                return cnt
            if i==end:
                print('turning point',end, 'will to', farthest)
                cnt += 1
                end = farthest
        return cnt

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
