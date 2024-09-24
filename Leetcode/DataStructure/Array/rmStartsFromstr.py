# 2390. Removing Stars From a String

# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
'''
Runtime: 128ms Beats 82.64%
Memory: 18.34MB Beats 14.75%

Time: O(n)
Space: O(1)

I use a stack structure.
I add characters in a List. If the character is a star, don't add it and remove the last character from the list. Otherwise, I add it to the list.
'''
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack+=[c]
        return "".join(stack)