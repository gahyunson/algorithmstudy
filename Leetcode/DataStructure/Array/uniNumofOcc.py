# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:

    '''
    Runtime: 43ms Beats 44.05%
    Memory: 16.65MB Beats 57.95%

    Time complexity: O(n)
    Space complexity: O(n)

    How to approach?

    - Use a dictionary (key-value form) to keep track of the number of occurrences of each element in the array.
    - The keys will represent the elements in the array, and the values will represent their corresponding counts.
    - After recording the counts, we want to ensure that all the counts (values) are unique.
    - To check this, compare the length of the list of values with the length of the set of values.
    If the lengths are the same, it means all the counts are unisque, so return 'True', Otherwise, return 'False'.
    '''
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = {}

        for i in arr:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
        return len(num.values()) == len(set(num.values()))

