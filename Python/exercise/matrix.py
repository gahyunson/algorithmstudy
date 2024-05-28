# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]

def matrix(n):
    results = []

    for i in range(n):
        add = []
        for j in range(n):
            add.append(j)
        results.append(add)

    # for i in range(n):
    #     results.append([], [], [])
    
    startRow = 0
    endRow = n-1
    startCol = 0
    endCol = n-1
    counter = 1

    while startRow <= endRow and startCol <= endCol :
        for i in range(startCol,endCol+1):
            results[startRow][i] = counter 
            counter += 1
        startRow += 1

        for i in range(startRow, endRow+1):
            results[i][endCol] = counter 
            counter += 1
        endCol -= 1

        for i in range(endCol, startCol-1, -1):
            results[endRow][i] = counter 
            counter += 1
        endRow -= 1

        for i in range(endRow, startRow-1, -1):
            results[i][startCol] = counter 
            counter += 1
        startCol += 1
    return results 

print(matrix(4))

# def test():
#     for i in range(10, -10, -1):
#         print(i)

# test()

