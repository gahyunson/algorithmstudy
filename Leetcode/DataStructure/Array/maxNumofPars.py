# 1679. Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        opr = 0
        ant = 0
        post = len(nums)-1
        
        while ant < post:
            print(nums, ant, post)
            nk =  nums[ant] + nums[post]
            if nk == k:
                ant += 1
                post -= 1
                opr += 1
            elif nk < k:
                ant += 1
            else:
                post -= 1

        return opr