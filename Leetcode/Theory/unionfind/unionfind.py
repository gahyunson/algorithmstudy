

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [i] * size 

    def find(self, x):
        if self.root[x] == x:
            return x 
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx 
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty 
            else:
                self.root[rooty] = rootx 
                self.rank[rootx] += 1 
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)