# 11. Container With Most Water 

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith the are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

'''
How to approach?

I used tow pointers.
Indexes start from 0 and end of the array.

The range of values is to 10 to the power of 4. 
Area could be greatest if a height is 10 to the power of 4 even a width is 1.
That's the reason I had to check all areas.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            area = (right-left)*min(height[left], height[right])
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area