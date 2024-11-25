# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Tow pointer

        Time complexity: O(n)
        Space complexity: O(len(word1) + O(len(word2)))

        Runtime 20ms Beats 99.64%
        Memory 16.65MB Beats 20.55%
        """
        max_i = max(len(word1), len(word2))
        i = 0
        result = ""

        while i < max_i:
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        """
        Runtime 38ms Beats 35.43%
        Memory 16.73MB Beats 20.55%
        """
        word1 = list(word1)
        word2 = list(word2)
        result = []
        while word1 and word2:
            result.extend([word1.pop(0), word2.pop(0)])

        if word1:
            result.extend(word1)
        if word2:
            result.extend(word2)

        result = "".join(result)

        return result






