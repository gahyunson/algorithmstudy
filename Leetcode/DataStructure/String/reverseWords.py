# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s:str) -> str:
        arr = s.split(' ')
        result = []
        for a in arr:
            if a:
                result.insert(0, a)
        return " ".join(result)
    
    
import unittest

class Test(unittest.TestCase):
    def test_reverse(self):    
        solution = Solution()
        input = "  hello world  "
        output = "world hello"

        self.assertEqual(solution.reverseWords(input), output)

if __name__ == '__main__':
    unittest.main()
        

