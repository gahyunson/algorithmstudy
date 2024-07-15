# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

'''
How to approach?

nums1, nums2 두 배열의 요소를 앞에서부터 하나씩 비교하였다.
총 길이가 짝수인 경우, 중간의 두 값을 합쳐야 했기 때문에 두 값을 저장할 수 있어야 해서, 직전의 요소를 저장할 수 있게 하였다.

1. initialize two pointers, i and j, both initially set to 0.
2. Move the pointer that corresponds to the smaller value forward at each step.
3. Continue moving the pointers until you have processed half of the total number of elements.
4. Calculate and return the median based on the values pointed to by i and j.

Time : O(n+m)
Space : O(1)
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        cur = 0
        pre = 0

        for cnt in range((m+n)//2+1):
            pre = cur 
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    cur = nums1[i]
                    i += 1
                else:
                    cur = nums2[j]
                    j += 1
            elif i < m :
                cur = nums1[i]
                i += 1
            elif j < n :
                cur = nums2[j]
                j += 1

        if (m+n) % 2 == 1:
            return cur 
        else:
            return (cur+pre)/2




        # if not nums1:
        #     return 

        # m = len(nums1)
        # n = len(nums2)
        # leNum = m + n
        # cnt = round(leNum/2)
        
        # nums = []
        # one = 0
        # two = 0
        # while one <= m-1 and two <= n-1 and len(nums) <= cnt:
        #     if nums1[one] <= nums2[two]:
        #         nums.append(nums1[one])
        #         one += 1
        #     elif nums1[one] > nums2[two]:
        #         nums.append(nums2[two])
        #         two += 1
        
        # if leNum % 2 == 1:
        #     return nums[-1]
        # else:
        #     if one == m:
        #         print(nums2[two])
        #         nums.append(nums2[two])
        #     elif two == n:
        #         print(nums1[one])
        #         nums.append(nums1[one])
        #     print(nums)
        #     return sum(nums[-2:])/2
        