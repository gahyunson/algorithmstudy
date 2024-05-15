# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = 1
        x = nums[0]
        counter = 1
        while index < len(nums):
            if nums[index] == x:
                counter = counter + 1
                if x == 0:
                    if counter > 3:
                        nums.pop(index)
                    else:
                        index = index + 1
                elif counter > 2:
                    nums.pop(index)
                else:
                    index = index + 1
            else:
                x = nums[index]
                counter = 1
                index = index + 1
        if(not all(n>0 for n in nums)):
            counts = Counter(nums)
            result = [[0,0,0]] if counts[0] >= 3 else []
            nums =[i for i in sorted(counts) if i!=0]
            if counts[0]>0:
                for i in nums:
                    if i>0:
                        break
                    if -i in counts:
                        result.append([-i , 0 , i])
            for i in nums:
                if i & 1:
                    continue
                remaining = -i >> 1
                if counts[remaining] >= 2:
                    result.append([i, remaining, remaining])
            for i, n in enumerate(nums):
                kk = -(nums[0] + n)
                if kk < n:
                    break
                j = bisect_right(nums, -n << 1) if n < 0 else i + 1
                k = bisect_right(nums, kk)
                for right in nums[j:k]:
                    left = -(n + right)
                    if left in counts:
                        result.append([left, n, right])
            del counts , nums
            return result
        else:
            return []

        # nums.sort()
        # triplets = set()
        # for i in range(len(nums)-2):
        #     firstNum = nums[i]
        #     j = i + 1
        #     k = len(nums)-1
        #     while j < k:
        #         secondNum = nums[j]
        #         thirdNum = nums[k]

        #         potentialSum = firstNum + secondNum + thirdNum
        #         if potentialSum > 0:
        #             k -= 1
        #         elif potentialSum < 0:
        #             j += 1
        #         else:
        #             triplets.add((firstNum, secondNum, thirdNum))
        #             j += 1
        #             k -= 1
        # return triplets

        # nums.sort()
        # result = []
        # for i in range(len(nums)-1):
        #     for j in range(1, len(nums)):
        #         if i<j:
        #             if -nums[i]-nums[j] in nums[j+1:]:
        #                 values = [nums[i],nums[j],-nums[i]-nums[j]]
        #                 if values not in result:
        #                     result.append(values)
        
        # return result

        
                        
            