# 121. Best Time to Buy and Sell Stock

'''
How to approach?

check 1. the minimum value of the array
check 2. the maximum result 

the maximum result
It have to check all the element e.g.
[7,1,5,3,6,4],

1, 5 and 1, 3 and 1, 6 and 1, 4
the profit value is going to be the greatest of them.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices[1:]:
            print('max:', profit, 'vs.', price-min_price)
            profit = max(profit, price-min_price)
            print('min:', min_price, 'vs.', price)
            min_price = min(min_price, price)
            print('price turn',price, ', result is:', profit, min_price)
        return profit



    #     i = 0
    #     profit = 0
    #     while i < len(prices):
    #         if prices[i] < prices[i]:
    #             profit -= prices[i]
    #             j = i+1
    #             print('before profit',profit, 'prices[i]', prices[i])
    #             while j < len(prices):
    #                 sell = max(profit+prices[j], profit+prices[j+1])
    #                 if prices[i] > prices[i+1]:
                        
    #                 j += 1  
    #             profit += sell
    #             i += j
    #             print('after profit:', profit, ', sell:', sell)
    #         else:
    #             i += 1
    #     return profit





    #     # buy = False
    #     # profit = 0
    #     # # for i in range(len(prices)-1):
    #     # #     print(prices[i], prices[i+1])
    #     # #     if buy and prices[i] < prices[i+1]:
    #     # #         profit -= prices[i]
    #     # #         buy = False
    #     # #     if prices[i] <= prices[i+1]:
    #     # #         profit += prices[i]
    #     # #         buy = True
    #     # i = 0
    #     # while i != (len(prices)-1):
    #     #     if prices[i] < prices[i+1]:
    #     #         profit -= prices[i]
    #     #         profit += prices[i+1]
    #     #         i += 2
    #     #     i += 1
    #     # return profit
                