# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

'''
How to approach?

We will return origin character so don't transform all string to upper or lower.

If you want to replace character, you have to access with index.
So I made 's' to list. 
I collect the vowels from string and will atach a character from the end of the list. -> pop()

They want the result as string, I transform to string again.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        vow = []
        for c in s:
            if c in vowels:
                vow.append(c)

        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vow.pop()
        return "".join(s)

# Output Limit Exceeded
    def reverseVowels2(self, s: str) -> str:
        # vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowels = 'aeiouAEIOU'
        s = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            if (s[left] in vowels) and (s[right] in vowels):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            print(s, left, right)
        return "".join(s)

