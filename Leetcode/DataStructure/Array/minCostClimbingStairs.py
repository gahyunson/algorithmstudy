# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

"""
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0]*(len(cost)+1)

        for i in range(2, len(cost)+1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])

        return min_cost[-1]