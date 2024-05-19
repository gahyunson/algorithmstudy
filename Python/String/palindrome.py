# // --- Directions
# // Given a string, return true if the string is a palindrome
# // or false if it is not.  Palindromes are strings that
# // form the same word if it is reversed. *Do* include spaces
# // and punctuation in determining if the string is a palindrome.
# // --- Examples:
# //   palindrome("abba") === true
# //   palindrome("abcdefg") === false

def palindrome1(str):
    rev = ''
    for s in str:
        rev = s + rev
    return str == rev

def palindrome2(str):
    rev = str.split()
    rev.reverse()
    rev = ''.join(rev)
    return str == rev

def palindrome3(str):
    str_len=len(str)
    return all(str[r]==str[str_len-r-1] for r in range(str_len))

print(palindrome3('abba'))
        
