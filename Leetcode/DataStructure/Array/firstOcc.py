# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
How to approach?

This problem ask what is the index if the needle occurence in haystack.
I chekced every strings in haystack with slice as needle's length.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # get the needle's length
        n = len(needle)

        # i'll check all substrings and the length of the substring is the length of the needle.
        for i in range(len(haystack)-n+1):
            # check if the current substring matches needle
            if haystack[i:i+n] == needle:
                return i
        # if no match was found, return -1
        return -1
