# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) === 51
#   reverseInt(981) === 189
#   reverseInt(500) === 5
#   reverseInt(-15) === -51
#   reverseInt(-90) === -9

import pdb 

def reverseInt(n):
    result = str(abs(n))[::-1]
    result = int(result)
    # breakpoint()
    if n < 0:
        result = result * -1
    
    return result 

def reverseInt2(n):
    rev = str(abs(n))
    result = ''
    neg = False 

    for r in rev:
        if r=='-':
            neg = True 
        else:
            result = r + result 
    reversedInt = int(result)
    if not neg:
        reversedInt = reversedInt * -1
    return reversedInt

print(reverseInt2(-51))
# pdb.run("reverseInt(-51)")