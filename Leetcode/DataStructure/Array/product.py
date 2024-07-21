# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # prefix
        for i in range(1, n):
            print(answer[i], nums[i-1], answer[i-1])
            answer[i] = nums[i - 1] * answer[i - 1]
            print('after', answer[i])

        # suffix
        R = 1
        product_list = []
        for i in range(n - 1, -1, -1):
            print('answer[i]:',answer[i], 'before R:',R, answer)
            answer[i] = answer[i] * R
            R *= nums[i]
            product_list.append(nums[i])
            print('after R:',R, product_list)
        
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
            