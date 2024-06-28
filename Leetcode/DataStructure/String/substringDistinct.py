'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)

        if not s:
            return 0
        
        sl = len(s) - 1
        cur = ""
        while sl:
            for i in range(sl, -1, -1):
                if (sl+i) < len(s):
                    # print("[", i, ":", sl+i,"]")
                    cur = s[i:sl+i]
                    if len(cur) == len(set(cur)):
                        # maxS = s[i:sl+i]
                        return len(cur)                        
            # print("-"*20)
            sl -= 1'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length

import unittest

class Test(unittest.TestCase):
    
    def test1(self):
        solution = Solution()

        input = "abcabcbb"
        output = 3
        self.assertEqual(solution.lengthOfLongestSubstring(input), output)

    def test2(self):
        solution = Solution()

        input = "bbbbb"
        output = 1
        self.assertEqual(solution.lengthOfLongestSubstring(input), output)

    def test3(self):
        solution = Solution()

        input = ""
        output = 0
        self.assertEqual(solution.lengthOfLongestSubstring(input), output)

    def test4(self):
        solution = Solution()

        input = " "
        output = 1
        self.assertEqual(solution.lengthOfLongestSubstring(input), output)

if __name__=='__main__':
    unittest.main()