# 22. Generate Parentheses

# Given n pairs of parentheses, write a funtion to generate all combinations of well-formed parentheses.

from typing import List


class Solution:
    # First approach using backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(n, left, right, cur):
            # Base case: when the current string length is 2*n and both left and right counts are equal to n
            if len(cur) == 2*n and left == n and right == n:
                result.append(''.join(cur)) # Join the current list of characters into a string and add to result
            
            # If there are left parentheses remaining to add
            if left < n:
                cur.append('(') # Add '(' to the current string
                backtrack(n, left+1, right, cur) 
                cur.pop() # Backtrack by removing the last character

            # If there are more right parentheses needed to balance the string
            if right < left:
                cur.append(')')
                backtrack(n, left, right+1, cur)
                cur.pop()
        # Start the backtracking process
        backtrack(n, 0, 0, [])
        return result 
    
    def generateParenthesis2(self, n: int) -> List[str]:
        def helper(result, s, left, right):
            if left == 0 and right == 0:
                result.append(s)
            if left > 0:
                helper(result, s+'(', left-1, right)
            if left < right:
                helper(result, s+')', left, right-1)
            
        result = []
        helper(result, "", n, n)
        return result