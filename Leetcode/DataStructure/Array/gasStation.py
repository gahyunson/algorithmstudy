# 134. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution:
    '''
        It is 'Greedy Algorithm'.
        If you compared sum(gas) and sum(cost), don't need to care before updated starting point. It's the reason could solve by O(n).

        We searching for starting point. If there was less than 0 at once, it couldn't work. so we pass it and try next index.

        If there is 0 or positive number once, it can be start point. 
        We check each tank each index - gas[i] , cost[i].
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1

        tank = start_idx = 0
        for i in range(len(gas)):
            # print('before tank + gas[i] - cost[i] =', tank, '+', gas[i], '-', cost[i])
            tank = tank + gas[i]-cost[i] 
            # print('after tank', tank)
            if tank < 0: 
                tank, start_idx = 0, i+1
            # print('and start_idx', start_idx)
        return start_idx 
    

    '''
    I want to check all element's sum but didn't work.
    '''
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     i = 1
    #     tank = 0
    #     while i <= len(gas):
    #         for j in range(i, len(gas)+1):
    #             # print('first',j)
    #             tank = tank + gas[j-1] - cost[j-1]
    #             print('first gas',gas[j-1], 'cost', cost[j-1], 'tank', tank)
    #             if tank < 0:
    #                 print('Im less than 0')
    #                 continue
            
    #         for j in range(1, i):
    #             # print('second',j)
    #             tank = tank + gas[j-1] - cost[j-1]
    #             print('second gas',gas[j-1], 'cost', cost[j-1], 'tank', tank)
    #             if tank < 0:
    #                 print('Im less than 0')
    #                 continue
    #         # if tank >= 0:
    #         #     return i
    #         print('i', i, 'tank', tank)
    #         i += 1
    #     return -1



