# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False


# def anagrams(stringA, stringB):
#     dict = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
#             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#             'a','b','c','d','e','f','g','h','i','j','k','l','m',
#             'n','o','p','q','r','s','t','u','v','w','x','y','z']
#     for a in stringA:
#         if a in stringB:
#             stringB.replace(a, '')
    
#     for b in stringB:
#         if b in dict:
#             return False
#     return True


import re

# using reg expression, dictionary...
# 정규표현식을 이용해서 알파벳만 남긴다.
# 알파벳이 무엇이 몇 개 있는지 딕셔너리에 등록한다.
# 두 개의 딕셔너리를 비교해서 완전히 똑같은지 확인한다.

# Use regular expressions to keep only alphabets
# Create two dictionaries to store the count of each alphabet
# compare two dictionaries to check if they are completely equal.
def anagrams3(stringA, stringB):    
    reA = sorted(re.sub(r'\W', '', stringA).lower())
    reB = sorted(re.sub(r'\W', '', stringB).lower())

    if len(reA) != len(reB):
        return False 
    
    dictA = {}
    for a in reA:
        if a not in dictA:
            dictA[a] = 1
        else:
            dictA[a] += 1
    dictB = {}
    for b in reB:
        if b not in dictB:
            dictB[b] = 1
        else:
            dictB[b] += 1

    for char in dictA:
        if dictA[char] != dictB[char]:
            return False
    return True 


# Use regular expressions to keep only alphabets
# And change the alphabets to lowercase
# And sort it to compare
# compare two strings
def anagrams2(stringA, stringB):
    return cleanString(stringA) == cleanString(stringB)

def cleanString(str):
    # in python, 'sorted' sorts 'string, tuple, list ... type'
    reStr = sorted(re.sub(r'\W', '', str).lower())
    return reStr

# Create a function to
# Use regular expressions to keep only alphabets
# And change to lowercase 
# Create a dictionary to count the alphabets.
# We can easily compare strings with the function.
def anagrams1(stringA, stringB):
    aCharMap = buildCharMap(stringA)
    bcharMap = buildCharMap(stringB)

    if len(aCharMap) != len(bcharMap) :
        return False
    for char in aCharMap:
        if aCharMap[char]!= bcharMap[char]:
            return False
    return True
def buildCharMap(str):
    charMap = {}
    for char in re.sub(r'\W', '', str).lower():
        if char not in charMap:
            charMap[char]=1
        else:
            charMap[char] += 1
    return charMap


print(anagrams2('hello', 'llohe'))
print(anagrams2('Whoa! Hi!', 'Hi! Whoa!'))
print(anagrams2('One One', 'Two two two'))
print(anagrams2('One one', 'One one c'))
print(anagrams2('A tree, a life, a bench', 'A tree, a fence, a yard'))

print(anagrams('hello', 'llohe'))
print(anagrams('Whoa! Hi!', 'Hi! Whoa!'))
print(anagrams('One One', 'Two two two'))
print(anagrams('One one', 'One one c'))
print(anagrams('A tree, a life, a bench', 'A tree, a fence, a yard'))