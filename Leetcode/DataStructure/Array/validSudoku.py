# 36. Valid Sudoku

'''
How to approach?

We can mark the information where it belong.
(i, element) means each row's information: (row number, value)
(element, j) means each column's information: (value, column number)
(i // 3, j // 3, element) means each of the nine 3x3 sub-boxes of the grid

if first row has numbers twice it will store as (1, 3), (1, 3).
So we can recognize it's wrong answer.
'''

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))