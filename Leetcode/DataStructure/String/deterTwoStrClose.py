# 1657. Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution:
    '''
    m < n

    Time: O(m)
    Space: O(m)

    Runtime: 69ms Beats 98.91%
    Memory: 17.97MB Beats 9.86%
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1 = {}
        w2 = {}
        for word in set(word1):
            w1[word] = word1.count(word)
            w2[word] = word2.count(word)
        
        return sorted(w1)==sorted(w2) and sorted(w1.values())==sorted(w2.values())
    
    '''
    Runtime: 122ms Beats 88.82%
    Memory: 17.99MB Beats 9.86%

    Time: O(n)
    Space: O(m)
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1 = Counter(word1)
        w2 = Counter(word2)

        return sorted(w1)==sorted(w2) and sorted(w1.values())==sorted(w2.values())

    '''
    1. The total length of the word1 equal to word2.
    2. The alphabets of word1 equal to word2.
    3. The number of the alphabet to be swapped is equal to the number of the alphabet being swapped to.

    Runtime: 182ms Beats 53.46%
    Memory: 17.46MB Beats 97.82%

    Time complexity: O(n+mlogm)
    Space: O(m)
    '''
    def closeStrings2(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): # O(1)
            return False
        
        if word1 == word2: # O(n)
            return True

        w1 = {}
        for word in word1: # O(n)
            if word in w1:
                w1[word] += 1
            else:
                w1[word] = 1

        w2 = {}
        for word in word2:
            if word in w2:
                w2[word] += 1
            else:
                w2[word] = 1

        return sorted(w1) == sorted(w2) and sorted(w1.values()) == sorted(w2.values()) # O(m logm)