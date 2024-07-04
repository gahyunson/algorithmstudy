# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

from typing import List


class Solution:
    # a backtracking approach, 가능한 해를 검색 (DFS, BFS와 다름)
    # stop when it finds the result. (It is not DFS, BFS)
    def combinationSum(self, candidates: List[int], target: int):
        def backtrack(remaining, combo, start):
            # Base case: if the remaining target is 0, we've found a valid combination!
            if remaining == 0:
                # add a copy of the current combination to the result list
                result.append(list(combo))
                return
            # if remaining target < 0, no valid combination can be formed
            elif remaining < 0:
                return 
            
            # iterate over the candidates , start ~
            for i in range(start, len(candidates)):
                # add the candidate -> the current combination
                combo.append(candidates[i])
                # recursively call backtrack with the updated remaining target
                # pass i, instead of i+1, it can reuse the same element
                backtrack(remaining - candidates[i], combo, i)
                # remove the last added candidate from the combination
                combo.pop()
        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result 

    
import unittest

class Test(unittest.TestCase):
    def test1(self):
        candidates = [2,3,6,7]
        target= 7
        output = [[2,2,3],[7]]

        solution = Solution()
        self.assertEqual(solution.combinationSum(candidates, target), output)

    def test2(self):
        candidates = [2, 3, 5]
        target= 8
        output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        solution = Solution()
        self.assertEqual(solution.combinationSum(candidates, target), output)

    def test3(self):
        candidates = [2]
        target= 1
        output = []

        solution = Solution()
        self.assertEqual(solution.combinationSum(candidates, target), output)

if __name__=='__main__':
    unittest.main()