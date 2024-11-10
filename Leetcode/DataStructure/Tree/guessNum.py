# 374. Guess Number Higher or Lower

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Runtime 22ms Beats 99.14%
        Memory 16.78MB Beats 10.20%

        Time complexity: O(logn)
        Space complexity: O(1)
        """
        min_n = 1
        max_n = n
        g = n

        while min_n<max_n and guess(g)!=0:
            g = (min_n + max_n)//2
            if guess(g)<0:
                max_n = g
            elif guess(g)>0:
                min_n = g
        return g

    def guessNumber2(self, n: int) -> int:
        """
        Time exceed
        """
        if n < 2:
            return n
        g = n//2

        while guess(g)!=0 and g > 0:
            if guess(g) < 0:
                g = g//2
            elif guess(g) > 0:
                g = g//2 + g
            print(g)

        return g


class Solution2:
    """
    Time exceed
    """
    def __init__(self, n):
        self.g = n//2

    # def guess(num: int) -> int:
    def guessNumber(self, n: int) -> int:
        if guess(self.g)==0:
            return self.g
        elif guess(self.g)==-1:
            self.g = self.g//2
            return self.guessNumber(n)
        elif guess(self.g)==1:
            self.g = self.g+((n-self.g)//2)
            return self.guessNumber(n)