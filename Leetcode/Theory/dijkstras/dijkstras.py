class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)

import heapq

class Graph:
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for _ in range(V)]
    
    def add_edge(self, u, v, w):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))
    
    def shortest_path(self, src):
        pq = [(0, src)] # [(the distance, the vertex label)]

        dist = [float('inf')]*self.V # a list for distance for comparing with shorter distances.
        dist[src] = 0

        # unil the pq(the priority queue) becomes empty
        while pq:
            # extract the first element in the tuple from the priority queue
            # the first element is the minimum distance vertex 
            current_dist, u = heapq.heappop(pq)

            for v, weight in self.adj[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight 
                    heapq.heappush(pq, (dist[v], v))
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

        

import unittest

class Test(unittest.TestCase):
    @unittest.skip("class Dijkstra")
    def test(self):
        graph = {
            'A': {'B': 10, 'C': 3},
            'B': {'C': 1, 'D': 2},
            'C': {'B': 4, 'D': 8, 'E': 2},
            'D': {'E': 7},
            'E': {'D': 9},
        }
        dijk = Dijkstra()
        dijk.dijk(graph, 'A')

    def test_graph(self):
        V = 9
        g = Graph(V)

        g.add_edge(0, 1, 4)
        g.add_edge(0, 7, 8)
        g.add_edge(1, 2, 8)
        g.add_edge(1, 7, 11)
        g.add_edge(2, 3, 7)
        g.add_edge(2, 8, 2)
        g.add_edge(2, 5, 4)
        g.add_edge(3, 4, 9)
        g.add_edge(3, 5, 14)
        g.add_edge(4, 5, 10)
        g.add_edge(5, 6, 2)
        g.add_edge(6, 7, 1)
        g.add_edge(6, 8, 6)
        g.add_edge(7, 8, 7)

        g.shortest_path(0)

if __name__=='__main__':
    unittest.main()