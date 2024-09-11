# 392. Is Subsequence

'''
I used two pointers.
One for stirng s, 무ㅇ the other one for stirng t.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is a substring of t, you can directly return True.
        if s in t:
            return True
        
        # you can scan the elements of both strings 's' and 't'.
        # If s[si] and t[ti] are same, it means that the current character of 's' is found in 't'.
        si = 0
        ti = 0
        while ti < len(t) and si < len(s):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        
        # If you've gone through all characters in 's', return True
        if si == len(s):
            return True
        return False
        
        


class Solution2:
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
        
                
