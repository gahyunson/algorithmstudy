# --- Directions
# Write a function that returns the number of vowels
# used in a string.  Vowels are the characters 'a', 'e'
# 'i', 'o', and 'u'.
# --- Examples
#   vowels('Hi There!') --> 3
#   vowels('Why do you ask?') --> 4
#   vowels('Why?') --> 0


def vowels1(str):
    vow = ['a','e','i','o','u']

    n = 0
    for char in str.lower():
        if char in vow:
            n+=1
    return n

import re 
# Regular expression
def vowels2(str):
    res = ''.join(re.findall('[aeiouAEIOU]+', str))

    result = len(res) if len(res) else 0
    return result 

print(vowels2('Hi There!'))
print(vowels2('Why do you ask?'))
print(vowels2('Why?'))