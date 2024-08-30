# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    # Runtime 264ms Beats 70.91%
    # Memory 25.71MB Beats 48.34%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        answer = [1] * len(nums)

        # answer[0] = 1
        # answer[1] = 1*nums[0]
        # answer[2] = 1*nums[0]*nums[1]
        # answer[3] = 1*nums[0]*nums[1]*nums[2]
        ant = 1
        for i in range(len(nums)):
            answer[i] = ant
            ant = ant*nums[i]
        
        # answer[3] = answer[3] * 1
        # answer[2] = answer[2] * nums[3]
        # answer[1] = answer[1] * nums[2] * nums[3]
        # answer[0] = answer[0] * nums[1] * nums[2] * nums[3]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * post
            post = post * nums[i]
        
        return answer
            


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # prefix
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]

        # suffix
        R = 1
        product_list = []
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * R
            R *= nums[i]
            product_list.append(nums[i])
        
        return answer
    
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     prefix = 1
    #     suffix = 1
    #     answer = [0] * n
    #     product_list = []

    #     for i in range(n):
    #         # print('before,',answer, prefix, nums)
    #         answer[i] = prefix
    #         prefix *= nums[i]
    #         product_list.append(nums[i])
    #         print('after,',answer, prefix, nums, product_list)
            
    #     product_list = []
    #     for i in range(n-1, -1, -1):
    #         answer[i] *= suffix
    #         suffix *= nums[i]
    #         product_list.append(nums[i])
    #         print(answer,i,suffix, product_list)
    #     return answer
            