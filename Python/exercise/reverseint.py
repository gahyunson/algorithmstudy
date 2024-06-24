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
    # First, convert the number into a string.
    # Use the absolute value to remove the minus sign, if present.
    result = str(abs(n))[::-1]
    # Then convert the string back into a integer.
    result = int(result)
    # breakpoint()
    # So if 'n' is grater than zero, than we want to just leave everything as is.
    # if 'n' is less than zero, then we want to multiply the result of this by negative one to turn it into a negative number.
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