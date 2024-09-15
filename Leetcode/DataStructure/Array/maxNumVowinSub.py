# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Runtime 169ms Beats 15.91% 
# Memory 17.34MB Beats 58.46%

'''
Time complexity: O(n)
Space complexity: O(1)

How to approach?

Window sliding tech.

It moves one step at atime.
As it moves, the first character of the current window is removed,
and the next character is added to the window.

If the removed character is a vowel, decrease cnt by one.
If the added character is a vowel, increase cnt by one.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        
        max_cnt = 0
        cnt = 0
        for c in s[:k]:
            if c in vowels:
                cnt += 1
        max_cnt = cnt
        
        for i in range(len(s)-k):
            s[i:i+k]
            if s[i] in vowels:
                cnt -= 1
            if s[i+k] in vowels:
                cnt += 1
            
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt
