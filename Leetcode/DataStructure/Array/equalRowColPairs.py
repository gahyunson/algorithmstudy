# 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution:
    '''
    Time: O(n**3)
    Space: O(1)
    '''
    def equalPairs(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # cnt = 0
        # equal = {}

        # for i in range(n):
        #     for j in range(n):
        #         for z in range(n):
        #             if j < z:
        #                 if grid[i][j] == grid[i][z]:
        #                     if (j,z) not in equal:
        #                         equal[(j,z)] = 1
        #                     else:
        #                         equal[(j,z)] += 1
        # print(equal)
        # return max(equal.values())
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt