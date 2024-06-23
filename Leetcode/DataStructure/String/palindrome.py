'''
9. Palindrome Number
Given an integer x, return true if x is palindrome, and false otherwise
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = list(str(x))
        strX.reverse()
        if strX == list(str(x)):
            return True
        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return all(x[i] == x[len(x)-i-1] for i in range(len(x)))
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        if x == x[::-1]:
            return True
        return False
        

import unittest

class Test(unittest.TestCase):
    def test_palindrome(self):
        solution = Solution()
        input = -121
        output = False

        self.assertEqual(solution.isPalindrome(input), output)

if __name__=='__main__':
    unittest.main()