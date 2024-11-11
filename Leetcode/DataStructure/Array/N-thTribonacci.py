# 1137. N-th Tribonacci Number

# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Bottom-up Dynamic Programming approach.

        Runtime 0ms Beats100.00%
        """
        t = [0,1,1]
        if n <= 2:
            return t[n]

        for _ in range(n-2):
            t.append(sum(t[-3:]))
        return t[-1]


    def tribonacci2(self, n: int) -> int:
        """Time Limit Exceeded"""
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)