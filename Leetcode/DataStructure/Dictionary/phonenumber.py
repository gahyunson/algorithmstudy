# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]



from typing import List

class Solution:
    def letterCombinations2(self, digits: str) -> List[str]:
        result = []
        phone = [[],[],list('abc'),list('def'),list('ghi'),list('jkl'),list('mno'),list('pqrs'),list('tuv'),list('wxyz')]

        allowed = list(map(int, list(digits))) # [2, 3]
        n = len(allowed) # 2
        if n==0:
            return result 
        
        def permute(curr, ind, allowed, digit):
            if ind == digit:
                result.append(curr)
                return 
            for j in phone[allowed[ind]]:
                permute(curr+j, ind+1, allowed, digit)
        permute("", 0, allowed, n)
        return result

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return 

        dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        if len(digits) == 1:
            return dict[digits]
        
        output=[]
        def backtrack(index:int, path:str):
            if index == len(digits):
                output.append(path)
                return
            possible_letters = dict[digits[index]]
            for letter in possible_letters:
                backtrack(index+1, path+letter)
        backtrack(0,"")
        return output
        

import unittest

class Test(unittest.TestCase):
    def test(self):
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        solution = Solution()
        self.assertEqual(solution.letterCombinations(digits), expected)

if __name__=='__main__':
    unittest.main()