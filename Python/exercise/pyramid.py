# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'    
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'

# 1 
# 0 1 0

# 2
# 1 1 1
# 0 3 0

# 3
# 2 1 2
# 1 3 1
# 0 5 0

# n
# ((2n-1)-1)/2 1 ((2n-1)-1)/2
# ... 
# 0 2n-1 0

def pyramid1(n):
    for i in range(1,n+1):
        print('_'*(n-i) + '#'*(2*i-1) + '_'*(n-i))

# row, column
def pyramid2(n):
    midpoint = (2*n-1)//2
    for row in range(n):
        level = ''
        for col in range(2*n-1):
            if midpoint-row <= col and col <= midpoint+row:
                level += '#'
            else:
                level += '_'
            col += 1
        row += 1
        print(level)

# Recursion
def pyramid3(n, row=0, level=''):
    if row == n:
        return;

    if len(level) == (2*n-1):
        print(level)
        return pyramid3(n, row+1)
    
    midpoint = (2*n-1)//2
    add = ''
    if midpoint-row <= len(level) <= midpoint+row:
        add = '#'
    else:
        add = '_'
    
    pyramid3(n, row, level + add)




pyramid3(3)