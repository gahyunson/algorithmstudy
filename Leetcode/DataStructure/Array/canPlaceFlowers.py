# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1]==0) and (i == len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                cnt += 1
                if cnt >= n:
                    return True
        return cnt >= n

        # cnt = 0
        # start = flowerbed.index(1)

        # zero = 0
        # for i in range(start, len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         zero += 1
        #     else:
        #         if zero >= 3:
        #             cnt += int(zero * (1/2) - (1/2))
        #         zero = 0
        
        # zero = 0
        # for i in range(start-1, -1, -1):
        #     if flowerbed[i] == 0:
        #         zero += 1
        #     else:
        #         if zero >= 3:
        #             cnt += int(zero * (1/2) - (1/2))
        #         zero = 0
        # print(cnt)
        # return cnt >= n
