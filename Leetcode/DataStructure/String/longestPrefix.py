# 14. Longest Common Prefix

'''
How to approach?

I minumized each element for comparison by sorting an array was consist of stirng elements.
It would sort by alphabetical order, the first and last elements diffe from all others.
This implies that there is no need to consider the other elements for comparison. I simply compared the first and last elements and obtained the result.

배열을 정렬하여 비교할 요소를 최대한 줄여보았다. 
알파벳 순서대로 배열을 정렬하면 요소가 비슷한 순서대로 정렬되는데
그러면 가장 양 끝에 있는 요소가 겹치는 알파벳이 가장 줄어들게 된다.
모든 배열의 요소들 중 겹치는 substring을 찾아내는 문제이므로 이 둘만 비교하여 
값을 추출하였다.
'''

from typing import List
import unittest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs.sort()
        left = strs[0]
        right = strs[-1]

        r = min(len(left), len(right))
        for i in range(r):
            if left[i]==right[i]:
                result += left[i]
            else:
                return result
        return result
        
class Test(unittest.TestCase):
    def test_str(self):
        solution = Solution()
        input = ["flower","flow","flight"]
        output = "fl"
        self.assertEqual(solution.longestCommonPrefix(input), output)

    def test_bl(self):
        solution = Solution()
        input = ["abc","def","kl"]
        output = ""
        self.assertEqual(solution.longestCommonPrefix(input), output)

if __name__=='__main__':
    unittest.main()