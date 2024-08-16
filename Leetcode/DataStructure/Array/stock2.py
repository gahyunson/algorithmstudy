# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

'''
How to approach?

This is Greedy Algorithm.

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        start = prices[0] 

        for i in range(len(prices)):
            if start < prices[i]:
                mx = mx + prices[i] - start
            start = prices[i] 
        return mx
    


'''
주어진 테스트 예제들을 보고 각 상황에 맞는 로직을 작성하였다.
그래서 코드가 길어졌다.
하지만 테스트를 통과하지 못했다.

I wrote logic for each test case based on the given 3 examples. So the became long.
However, it didn't pass the tests.
'''
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         buy = 0

#         for i in range(1, len(prices)):
#             if not buy and prices[i-1] > prices[i]:
#                 print('if:', prices[i-1], prices[i])
#                 continue
#             elif prices[i-1] <= prices[i]:
#                 profit -= prices[i-1]
#                 buy = 1
#                 print('elif:', prices[i-1], prices[i])
#                 print('prices[i-1]:', prices[i-1], ', profit:', profit)
#                 ck = prices[i:]
#                 if len(ck)>2:
#                     for j in range(1, len(ck)):
#                         # print('in ck:', ck[j-1], ck[j])
#                         if ck[j-1] < ck[j]:
#                             print('if ck:', ck[j-1], ck[j], j)
#                             if j == len(ck)-1:
#                                 profit += ck[j]
#                                 return profit 
#                             continue 
#                         elif ck[j-1] > ck[j]:
#                             profit += ck[j-1]
#                             break
#                 else:
#                     profit += prices[i]
#         return profit
            

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
