# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

'''
How to approach?

We need the first of each the words. But can't use the function 'pop' on string type.
So I transformed to List type. 

I extracted the first letter of the words and add it to the result.

If the length are different between word1 and word2, 
The rest of word don't have to pop. just transform it to String type again.

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1 = list(word1)
        word2 = list(word2)

        while word1 and word2:
            result += word1.pop(0)
            result += word2.pop(0)

        if word1:
            result += "".join(word1)
        elif word2:
            result += "".join(word2)

        return result

