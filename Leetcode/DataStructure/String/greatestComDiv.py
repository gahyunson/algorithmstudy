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
