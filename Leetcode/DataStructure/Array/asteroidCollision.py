# 735. Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

'''
Runtime: 86ms Beats 34.04%
Memory: 17.92MB Beats 9.75%

Time Complexity: O(n**2)
Space Complexity: O(1)
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for a in asteroids:
            while result and result[-1] > 0 and a < 0:
                if result[-1]+a > 0:
                    break
                elif result[-1]+a < 0:
                    result.pop()
                else:
                    result.pop()
                    break
            else:
                result.append(a)
        return result
                

        # result = [asteroids[0]]

        # for i in range(1, len(asteroids)):
        #     if result[-1] > 0 and asteroids[i] < 0:
        #         if abs(result[-1])==abs(asteroids[i]):
        #             result.pop()
        #         elif abs(result[-1]) > abs(asteroids[i]):
        #             continue 
        #         else: 
        #             result.pop()
        #             result.append(asteroids[i])
        #     else:
        #         result.append(asteroids[i])


        
        # return result
