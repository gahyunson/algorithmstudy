# 933. Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

'''
Runtime 201ms Beats 35.04%
Memory 22.37MB Beats 6.77%

Time Complexity: O(n)
Space Complexity: O(1)
'''
class RecentCounter:
    def __init__(self):
        self.req = []
        self.start = 0
        

    def ping(self, t: int) -> int:
        self.req.append(t)
        
        while self.req[self.start] < t-3000:
            self.start += 1
        return len(self.req) - self.start
    
'''Time Limit Exceeded'''
class RecentCounter2:

    def __init__(self):
        self.req = []        

    def ping(self, t: int) -> int:
        self.req.append(t)
        
        for i in range(len(self.req)):
            if self.req[i] in range(t-3000, t+1):
                return len(self.req)-i
        return None