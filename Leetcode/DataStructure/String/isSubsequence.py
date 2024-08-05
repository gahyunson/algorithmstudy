# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        elif not t:
            return False
        
        tn = len(t)
        sn = len(s)

        i = 0
        j = 0
        while i < tn and j < sn:
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                i += 1

        if j == sn:
            return True
        return False
        
                
