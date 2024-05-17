# 1. reverse() helper
def reverse1(str):
    str_list = str.split('')
    str_list.reverse()
    return "".join(str_list)

# 2. for loop helper
def reverse2(str):
    reversed = ''
    for s in str:
        reversed = reversed + s
    return reversed 

# 3. reduce heloper
from functools import reduce 
def reverse3(str):
    return reduce(lambda reversed, char: char + reversed, str, '')

# test
result = reverse3('hello')
print(result) 
print(type(result))