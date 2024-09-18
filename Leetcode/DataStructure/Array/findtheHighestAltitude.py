# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

'''
Runtime: 32ms Beats90.59%
Memory: 16.45MB Beats 62.64%

Time complexity: O(n)
Space complexity: O(1)

How to approach?
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0
        for g in ([0]+gain):
            alt += g
            if alt > max_alt:
                max_alt = alt
        
        return max_alt