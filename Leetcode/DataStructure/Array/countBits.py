# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        arr = []
        for i in range(n+1):
            bi = bin(i)
            arr.append(bi.count('1'))
        return arr
