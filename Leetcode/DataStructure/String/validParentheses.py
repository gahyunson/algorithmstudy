# 20. Valid Parentheses
#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        (())[] -> ())[] , (
        -> ))[] ,(( 
        -> [] , ((
        -> ] , (([
        -> 
        
        '''
        if len(s)%2==1:
            return False

        char = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        while s:
            cur = s[0]
            s = s[1:]
            if cur in char.values():
                stack.append(cur)
            else:
                if not stack or stack.pop() != char[cur]:
                    return False
        return not stack
            

                
