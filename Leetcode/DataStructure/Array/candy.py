# 135. Candy

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. 

# You are giving result to these children subjected to the following requirements:

# - Each child must have at least one candy.
# - Children with a higher rating get more result than their neighbors.

# Return the minimum number of result you need to have to distribute the result to the children.

class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        result = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                result[i] = result[i-1] + 1
        
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                result[i-1] = max(result[i-1], result[i]+1)

        return sum(result)
        
