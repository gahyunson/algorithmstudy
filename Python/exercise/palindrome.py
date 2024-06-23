# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("abba") === true
#   palindrome("abcdefg") === false

# be asked to return True or False to indicate whether or not this is a palindrome.


def palindrome1(str):
    rev = ''
    for s in str:
        rev = s + rev
    return str == rev

def palindrome2(str):
    # I'm going to do here is to split the string and then can use reverse function.
    rev = str.split()
    rev.reverse()
    # Join the reversed list and then we can see reversed string.
    rev = ''.join(rev)
    # return boolean value, if string is equal to the value of reversed then it will return True. Otherwise if it's not equal to each other, it will return False.
    return str == rev 

'''
The all() function checks all the elements of the values.
it will return True if all the elements are True.
if there is one False among the values it will return False.

This function compares the first element with the last element,
then the second with the second-to-last, and so on.
Indexes start with 0, so the end index of a string is the string's length minus 1.

Example indexing for comparison:
- start index 0 end index string's length - 1
- start index 1 and index string's length - 1 - 1
- start index 2 and index string's length - 1 - 1 - 1 
- start index 3 and index string's length - 1 - 1 - 1 - 1
- start index 3 and index string's length - 1 - 3

This pattern continues until the middle of the string is reached.
We can make the formular as r and shtring'slength-1-r
'''
def palindrome3(str):
    str_len=len(str)
    return all(str[r]==str[str_len-r-1] for r in range(str_len))

print(palindrome3('abba'))
        
