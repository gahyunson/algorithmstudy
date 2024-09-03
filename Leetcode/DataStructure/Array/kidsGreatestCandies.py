# 1431. Kids With the Greatest Number of Candies

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

'''
How to approach?

I confused meaning of 'the greatest number of candies among all the kids'.
I thought it means comparing with side numbers.
Actually that was 'greatest' number of the candies. 
So I just need maximum number of the candies.

I comapared with maximum number of the candies array.
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        m = len(candies)
        result = [True]*m

        for i in range(m):
            if candies[i]+extraCandies < greatest:
                result[i]=False
        return result

        # m = len(candies)
        # result = [True]*m

        # left = -1
        # right = 1

        # for i in range(len(candies)):
        #     if left == -1:
        #         if candies[i]+extraCandies < candies[right]:
        #             result[i] = False
        #         right += 1
        #     elif right < m:
        #         if candies[i]+extraCandies < candies[left] or candies[i]+extraCandies < candies[right]:
        #             result[i] = False
        #         right += 1
        #     else:
        #         if candies[i]+extraCandies < candies[left]:
        #             result[i] = False
        #     left += 1