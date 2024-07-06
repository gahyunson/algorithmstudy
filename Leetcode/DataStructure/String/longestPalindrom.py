# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

'''
How to approach?

Check all the substrings of the string.
If a longer palindrome is found, update 'maxStr' to that substring.

문자열에서 나올 수 있는 모든 substring의 경우의 수를 체크한다.
만약 길이가 더 긴 palindrom의 경우 결과값을 저장하는 maxStr를 업데이트한다.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s

        maxLen = 1
        maxStr = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if maxLen < len(s[i:j+1]) and s[i:j+1]==s[i:j+1][::-1]:
                    maxLen = j+1-i
                    maxStr = s[i:j+1]
        return maxStr


