# # Day 10 (Sep 22)
# ### 977. Squares of a Sorted Array

# I solved this problem using sorting.

# The given code aims to square each element of the input integer list 'nums', then sort the resulting squared values in ascending order, and finally return the sorted list.

# 1. Suqaring the Elements
# - The code starts by iterating through each element of the input list 'nums' using a list comprehension.
# - It squares each element using the expression 'num**2' and stores the squared values in a new list.

# 2. Sorting the Squared Values
# - After obtaining the squared values, the code proceeds to sort the new list in ascending order.
# - This is achieved using the 'sort()' method, which arranges the elements in non-decreasing order.

# 3. Returning the Sorted List
# - Finally, the code returns the sorted list of squared values as the result of the 'sortedSquares' function.

# complexity : O(n+n*log(n))

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num**2 for num in nums]
        nums.sort()
        return nums
