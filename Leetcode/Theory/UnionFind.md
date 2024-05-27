# Union-Find (Disjoint Set) 
- Data structure
- ex) Connect to the Network, Minimum Spanning Tree, image
- Union 합집합 연산, Find 특정 원소가 속한 집합 search
- don't have any element in common.

### 3 Operations
1. Make Set 
- 각 원소를 독립적 집합으로 만든다. 
- 각 원소는 루트인 트리로 표현.
2. Find
- 특정 원소가 속한 집합 대표(root) search 
- Path Compression 
3. Union 
- 각 두 원소가 속한 집합을 합친다

**PROCESS**
1. Adding new sets to the disjoint set
2. Merging disjoint sets to a single disjoint set using Union operation
3. Finding representative of a disjoint set using Find operation
4. Check if two sets are disjoint or not    

1. disjoint set에 new sets를 추가한다
2. disjoint sets가 단 하나의 집합이 되도록 Union 연산으로 합해준다
3. Find 연산을 통해 disjoint set 을 대표하는 것을 찾는다
4. 마지막으로 disjoint가 두개의 집합인지 아닌지 체크한다


### Find
- Time complexity : O(n)
```python
def find(i):
    # If i is the parent of itself 
    if parent[i] == i :
        # Then i is the representative of this set.
        return i
    else:
        return find(parent[i])
```

### Union
1. input : two elements
2. finds the representatives of their sets 
3. puts either one of the trees 
- Time complexity : O(n)

```python
# the set that includes i + the set that includes j
def union(parent, rank, i, j):
    # Find the representatives 
    irep = find(parent, i)
    jrep = find(parent, j)

    # Make 
    # the parent of i's representative -> j's representative 
    # moving all of i's set into j's set
    parent[irep] = jrep
```

- The efficiency depends heavily o which tree get attached to the other. -> Path Compression
- 어떤 set에 어떤 set을 잇느냐에 따라 효율성이 달라진다
- Union by Rank, Union by Size 

**Compressing the height** of the trees
```python
def find(i):
        if Parent[i]==i:
            return i
        else:
            result = find(Parent[i])
            Parent[i] = result
            return result
```
- Time complexity : O(log n)



[Reference Link]('https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/')