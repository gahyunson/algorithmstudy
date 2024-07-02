# Dijkstra's Algorithm (다익스트라 알고리즘 )

- Shortest path algorithm : Finds the path with the minimum cost.
- Start and end points are predetermined.
- V vertices, E edge : time complexity is O(E*logV).
- The cost at the start point is always 0.


* 최단 경로 알고리즘. 최소 비용이 드는 경로를 찾는다.
* 시작점과 도착점이 지정되어 있다.
* 정점 V개, 간선 E개 : 시간 복잡도 O(ElogV)
* 시작점의 비용은 항상 0이다. 

## Processing Steps (처리 과정)

1. For vertices [0, 1, 2, 3, 4, 5], if 0 is the starting point,
the initial costs are set as [0, inf, inf, inf, inf, inf].

    *If start point is 0 in [0, 1, 2, 3, 4, 5] graph,
    the cost are [0, inf, inf, inf, inf, inf].*

    0, 1, 2, 3, 4, 5 정점에 대하여 0이 시작점이면,
    비용이 [0, inf, inf, inf, inf, inf] 으로 시작한다.


2. The cost is updated only for vertices adjacent to the starting point. Vertices not adjacent are not updated.    
- Updated Costs: [0, 7, 9, inf, inf, 14]

    *It will update the cost only adjacented at start point, won't update not djacented.*

    0과 인접한 점에 대해서만 cost update, 결정된 경로과 인접하지 않은 정점은 업데이트하지 않는다.

3. Select vertex 1 as it has the lowest cost from the starting point. The costs are updated as needed, except for those vertices that were not choosen.
- Current Costs: [0, 7, 9, inf, inf, 14]

    *I'm going to choose 1 vertex that smallest cost from start point.
    It will update again the cost what determined except weren't choose.*

    최소 비용이 드는 정점 1을 선택한다.
    [0, 7, 9, inf, inf, 14] 업데이트된 비용은 그대로 두고 필요하면 업데이트한다.

4. Repeat the process until the endpoint is reached.
- Updated Costs: [0, 7, 9, 22, inf, 14]

    *Doing the same work till reach the end point.*

    끝점에 다다를 때까지 반복한다.


5. Further updateds to the costs. [0, 7, 9, 20, inf, 11]

6. [0, 7, 9, 20, 20, 11]

7. [0, 7, 9, 20, 20, 11]    
This is the minimum cost between vertices 0 and 5.   
0과 5정점 사이의 거리 최소비용



## Implementation (구현하기)

- Priority Queue

* 우선순위 큐

### Queue vs. Priority Queue
- Queue: The oldest element is dequeued first.
    FIFO
- Priority Queue: The highest priority is dequeued.
There is difference based on a defined standard.