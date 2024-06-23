import math

def build_sparse_table(arr):
    n = len(arr) # Number of elements in the input array
    k = math.floor(math.log2(n)) + 1 # Calculate the number of levels in the Sparse Table (log base 2 of n, plus one for inclusive level)
    st = [[0] * k for _ in range(n)] # Initialize the Sparse Table with 0s
    
    # Initialize the first column of the table with the input array elements
    # This corresponds to the interval length of 1 (base case)
    for i in range(n):
        st[i][0] = arr[i]
    
    # Build the Sparse Table
    j = 1
    # (1 << j) is 2 raised to the power j. Loop until 2^j is less than or equal to n
    while (1 << j) <= n:
        i = 0
        # Populate the table with the minimum value for the range covered by 2^j
        while (i + (1 << j) - 1) < n:
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
            i += 1
        j += 1
    return st

def query(st, L, R):
    # Compute the largest power of 2 that fits within the interval length
    j = math.floor(math.log2(R - L + 1))
    # Return the minimum value from the Sparse Table for the range [L, R]
    # Uses the precomputed values to find the minimum efficiently
    return min(st[L][j], st[R - (1 << j) + 1][j])

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
st = build_sparse_table(arr)
print(query(st, 0, 4))  # 0 
# print(query(st, 4, 7))  # 3 
# print(query(st, 3, 3))  # 0 