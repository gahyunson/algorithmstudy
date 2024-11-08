# Day 9
### 169. Majority Element
# I just wanna count all the values , because I have been analysis the data with python.
# There was so many columns and values , I can count each values. and then I can visualize the data.
# That's why I was thought I wanna know the count of all values.
# But there was hint for easy way. All the list have the count of majoristic value is always more than half of list length. If I look at the middle index value of the list , the value of major element always fill more than half of value length.


# The majority element is the element that appears more than [n/2] times. You may assume that the majority element always exists in the array.
# -> we can use index [n/2]
# -> we don't think about the same count of values


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        dis_nums = set(nums)
        result = dict()

        for dis in dis_nums:
            result[dis] = 0

        for num in nums:
            result[num] += 1

        for res in result:
            if result[res] == max(result.values()):
                return res

        return nums[n//2]
