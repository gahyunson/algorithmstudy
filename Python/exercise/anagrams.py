# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False
import re

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


def anagrams2(stringA, stringB):
    return cleanString(stringA) == cleanString(stringB)

def cleanString(str):
    # in python, 'sorted' sorts 'string, tuple, list ... type'
    reStr = sorted(re.sub(r'\W', '', str).lower())
    return reStr

# print(cleanString('hello !ee'))

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

# print(anagrams1('hello', 'llohe'))
# print(anagrams1('Whoa! Hi!', 'Hi! Whoa!'))
# print(anagrams1('One One', 'Two two two'))
# print(anagrams1('One one', 'One one c'))
# print(anagrams1('A tree, a life, a bench', 'A tree, a fence, a yard'))

# print(anagrams2('hello', 'llohe'))
# print(anagrams2('Whoa! Hi!', 'Hi! Whoa!'))
# print(anagrams2('One One', 'Two two two'))
# print(anagrams2('One one', 'One one c'))
# print(anagrams2('A tree, a life, a bench', 'A tree, a fence, a yard'))

print(anagrams3('hello', 'llohe'))
print(anagrams3('Whoa! Hi!', 'Hi! Whoa!'))
print(anagrams3('One One', 'Two two two'))
print(anagrams3('One one', 'One one c'))
print(anagrams3('A tree, a life, a bench', 'A tree, a fence, a yard'))