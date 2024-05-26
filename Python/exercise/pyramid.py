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
    for i in range(n+1):
        print(' '*(n-i) + '#'*(2*i-1) + ' '*(n-i))

pyramid1(3)