# 2215. Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.



class Solution:
    # Runtime: 142ms 56.76%
    # Memory: 17.05MB Beats 32.81%
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        return [n1-n2, n2-n1]

    # Runtime: 625ms Beats 9.24%
    # Memory: 16.97MB 64.17%
    def findDifference2(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]

        for num in nums1:
            if num not in answer[0] and num not in nums2:
                answer[0].append(num)
            
        
        for num in nums2:
            if num not in answer[1] and num not in nums1:
                answer[1].append(num)
        return answer

            