# 7. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(1)
        Space complexity: O(1)

        Runtime 0ms Beats 100.00%
        Memory 17.46MB Beats 8.20%
        """
        return bin(int(a, 2)+int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(len(a)+len(b))
        Space complexity: O(len(a)+len(b))

        Runtime 7ms Beats 5.52%
        Memory 17.53MB Beats 8.20%
        """
        a10 = 0
        for i in range(len(a)):
            print(i, a[i])
            a10 += int(a[i])*(2**(len(a)-i-1))

        b10 = 0
        for i in range(len(b)):
            b10 += int(b[i])*(2**(len(b)-i-1))

        return bin(a10 + b10)[2:]