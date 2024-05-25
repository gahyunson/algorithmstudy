# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'

def steps1(n):
    # From 0 to n
    for i in range(n):
        # string sequence is '#', ' '
        # print '#'*count , ' '*count
        # We need 'count'
        # '#' count is start at 1 and end 'n'
        # ' ' count is start at 'n-1' and end '0'
        # print('#'*(i+1) + ' '*(n-i-1))
        print('#'*(i+1) + '_'*(n-i-1))
    
# row and column
def steps2(n):
    # From 0 to n (iterate through rows)
    for row in range(n):
        # Create an empty string 'stair'
        stair = ''
        # From 0 to n (iterate through columns)
        for column in range(n):
            # IF the current column is equal to or less than the current row
            if column <= row:
                # Add a '#' to 'stair'
                stair += '#'
            else:
                # Add a space to 'stair'
                stair += ' '
        # print 'stair'
        print(stair) 

# recursive
def steps3(n, row = 0, stair = ''):
    if n==row:
        return;

    # pass to next row
    if n == len(stair):
        print(stair)
        return steps3(n, row + 1)

    # completing the current row
    '''if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '

    steps3(n, row, stair)   '''
    add = '#' if len(stair) <= row else ' '
    steps3(n, row, stair + add)
    
steps3(3)
