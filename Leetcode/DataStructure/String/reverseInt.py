# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution2:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        if result< -2**31 or result> 2**31-1:
            return 0
        if x <0:
            result = result * -1

        return result

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        reversed_int = int(str(abs(x))[::-1])

        if reversed_int > 2**31-1:
            return 0
        if is_negative:
            return -reversed_int
        return reversed_int
    
import unittest

class Test(unittest.TestCase):
    def test_num(self):
        solution = Solution()
        input = 1534236469
        output = 0
        self.assertEqual(solution.reverse(input), output)

    def test_minus(self):
        solution = Solution()
        input = -123
        output = -321
        self.assertEqual(solution.reverse(input), output)
    
    def test(self):
        solution = Solution()
        input = 120
        output = 21
        self.assertEqual(solution.reverse(input), output)

if __name__=='__main__':
    unittest.main()