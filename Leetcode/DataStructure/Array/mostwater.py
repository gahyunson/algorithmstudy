# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

'''
How to approach?

Extract the x and y values for the left and right points and calculate the area.
Traverse all x values for both left and right points to find the maximum area.
Since higher y values are more desirable, if one y value is lower, move the corresponding x coordinate.

left, right의 x, y 값을 추출하여 넓이를 구한다.
left, right의 값은 모든 x값을 거친다. 가장 넓은 값을 찾기 위해.
y값이 높을 수록 좋기 때문에 y값이 더 낮은 경우 x좌표 값을 움직인다.
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0

        while left < right:
            cur = (right - left)* min(height[left], height[right])
            maxArea = max(maxArea, cur)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea