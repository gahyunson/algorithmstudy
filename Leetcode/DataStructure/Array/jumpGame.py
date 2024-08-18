# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

'''
Below is the sum of element's index and its value. The result could be True if it reach 'Goal'.

Example 1: [2,3,1,1,4]

0 2 total energe: 2 (2>=1(Fourth Goal) so pass) -> return True
1 3 total energe: 4 (4>=2(Third Goal) so pass)
2 1 total energe: 3 (3>=3(Second Goal) so pass)
3 1 total energe: 4 (4>=4(Final Goal) so pass, something should reach here)
4 4 Final Goal

Example 2: [3,2,1,0,4]

0 3
1 2
2 1
3 0 total energe: 3 (3!>=4 can't pass) -> return False
4 4 Final Goal

1. Initialization
- The goal is initially set to the last index, which is the index we need to reach.

2. Iteration
- Start iterating from the second last element to the first element.
- For each element, check if the current index plus the jump length from that index is greater than or equal to the current goal.
- If it is, update the 'goal' to the current index because it means we can reach the current goal from this index.

3. Final Check
- After the iteration, if the goal if '0', this is the result of the  goal updated.
- Return 'True' if the goal is '0', otherwise return 'False'
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= goal:
                goal = i
        return True if goal==0 else False
    
'''
The bigger number is better to reach to the end of the array.
So, if there is bigger than before, reinitial 'n'.
-1 is the value of movement to next index.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = 0
        for num in nums:
            if n < 0:
                return False
            elif n < num:
                n = num
            n -= 1
        return True