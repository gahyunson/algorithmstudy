# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        
        len1 = len(nums1)
        end_idx = len1-1

        while n>0 and m>0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n-=1
            else:
                nums1[end_idx] = nums1[m-1]
                m-=1
            end_idx -= 1
        
        while n > 0:
            nums1[end_idx]= nums2[n-1]
            n-=1
            end_idx -= 1

        # mi = min(len(nums1), len(nums2))
        # one = 0
        # two = 0
        # while nums1 and nums2:
        #     if nums1[one] <= nums2[two]:
        #         print(nums1, '<=', nums2)
        #         one += 1
        #     elif nums1[one] > nums2[two]:
        #         print(nums1, '>', nums2)
        #         nums1[one+1:] = nums1[one:]
        #         nums1[one] = nums2.pop(two)
        #         two += 1
            
            