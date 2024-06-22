# // --- Directions
# // Given a string, return a new string with the reversed
# // order of characters
# // --- Examples
# //   reverse('apple') === 'leppa'
# //   reverse('hello') === 'olleh'
# //   reverse('Greetings!') === '!sgniteerG'

import pdb

# 1. reverse() helper
def reverse1(str):
    # i'm working with a array of characters
    str_list = str.split() 
    # reverse all the elements within the array
    str_list.reverse()
    # join it all back together again
    return "".join(str_list)

# 2. for loop helper
def reverse2(str):
    # start off by declaring a temporary variable 
    reversed = ''

    # the string - str - that we got passed in as an argument
    # create a temporary variable that is redeclared every single time through the loop of character.
    # i'm iterating through all of the characters of the string variable.
    for s in str:
        # the character added on to the start of the string reversed
        reversed = s + reversed
        # breakpoint()
    # after for loop I return the string reversed
    return reversed 

# 3. reduce heloper
from functools import reduce 

def reverse3(str):
    '''
    The reduce function from the functools module helps us reverse the string.
    using lambda function.

    It works by iterating through each character of the string.
    The lambda function specifies how to combine each character with the result accumulated so far.
    The lambda takes two arguments: 'reversed' (the accumulated result) and 'char' (the current character).
    For each character, the lambda function adds 'char' to the beginning of 'reversed'.
    I'm going to put the result to 'reversed' vaiable.
    The result is a new string with the characters in reverse order.
    '''

    return reduce(lambda reversed, char: char + reversed, str, '')

# test
result = reverse2('hello')
print(result) 
print(type(result))

pdb.run("reverse2('hello')")