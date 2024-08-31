# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

'''
Now I can explain it...

It was so difficult because I considered some examples not included in this problem.
For example str1 = "ABC", str2 = "ADE". this is not for this problem.

They will give you only example repeated strings.
They said 's = t+t+t+t+..+t'. It means they will always give us the example repeated.

So you don't have to worry all the substrings.

Example 1:
you can transform it to 
str1 = x + x , str2 = x
(ABC + ABC) , (ABC)
They required the value 'x' so str1 - x = x 
len(str1-x) is equal with len(str2)

Example 2:
str1 = (AB + AB + AB) = x + x + x , str2 = (AB + AB) = x + x .
We need x value. 
str1 - (x + x) = x = str1 - str2 = x 
so you can make it by str1[len(str2):]
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If both strings have the same length, check if they are identical.
        # If they are, then one of them is the greatest common divisor.
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""

        # Check if the concatenation of str1 and str2 is the same as str2 and str1.
        # If not, it means there is no common string that can divide both,
        # because if a string x can divide both, then any concatenation should be commutative.
        if str1 + str2 != str2 + str1:
            return ""
        
        # If str1 is longer than str2, recursively check for the gcd of the substring of str1
        # that excludes the prefix equal to str2, and str2 itself. This is equivalent to 
        # subtracting str2 from str1 until str1 is shorter than or equal to str2.
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        # If str2 is longer, do the reverse: subtract str1 from str2 and find the gcd.
        return self.gcdOfStrings(str1, str2[len(str1):])
