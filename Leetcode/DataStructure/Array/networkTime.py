# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Dijkstra's Algorithm - Priority Queue

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the graph
        graph = {i: [] for i in range(1, n+1)}
        for check_idx, v, w in times:
            graph[check_idx].append((v, w))

        # Distance to each node, initialized to infinity
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        # Min-heap priority queue
        adjacent_vertex = [(0, k)]  # (distance, node)

        while adjacent_vertex:
            distance, check_idx = heapq.heappop(adjacent_vertex)
            print('distance:', distance, ', check_idx:' , check_idx)
            print('dist:', dist)
            if distance > dist[check_idx]:
                print('distance > dist[u] : ',distance,'>',dist[check_idx])
                continue
            # It will not have error even though there is no any element adjusted.
            # There is not element graph[1] , when d, u = (1, 1). so This for loop will not excute
            for v, weight in graph[check_idx]:
                print('v:', v, ", weight:", weight, ", graph[check_idx]:", graph[check_idx])
                print('dist[check_idx] + weight =',dist[check_idx],'+',weight,'< dist[v]=',dist[v])
                if dist[check_idx] + weight < dist[v]:
                    dist[v] = dist[check_idx] + weight
                    heapq.heappush(adjacent_vertex, (dist[v], v))
                    print('adjacent_vertex:',adjacent_vertex)
            print('-'*30)
        # Get the maximum distance to any node
        max_dist = max(dist.values())

        if max_dist < float('inf'):
            return max_dist
        else:
            return -1
                
            
'''
# This section is my first idea.
        time[i] = (the source node, target node, time)
        times= [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n= 4
        k= 2
        cur = float('inf')
        for time in times:
            if time[0]==k:
                pre = time[1]
                if time[1]==n:
                    return time[2]
                for t in times:
                    if t[0]==time[1] and t[1]==time[1]:
                        return t[2]
            else:
                return -1
'''

import unittest
                
class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        output = 2

        self.assertEqual(solution.networkDelayTime(times, n, k), output)

if __name__=='__main__':
    unittest.main()