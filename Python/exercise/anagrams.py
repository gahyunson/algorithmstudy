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

def anagrams2(stringA, stringB):
    return cleanString(stringA) == cleanString(stringB)

def cleanString(str):
    reStr = re.sub(r'\W', '', str).lower().split().sort()
    return reStr



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

print(anagrams1('hello', 'llohe'))
print(anagrams1('Whoa! Hi!', 'Hi! Whoa!'))
print(anagrams1('One One', 'Two two two'))
print(anagrams1('One one', 'One one c'))
print(anagrams1('A tree, a life, a bench', 'A tree, a fence, a yard'))

print(anagrams2('hello', 'llohe'))
print(anagrams2('Whoa! Hi!', 'Hi! Whoa!'))
print(anagrams2('One One', 'Two two two'))
print(anagrams2('One one', 'One one c'))
print(anagrams2('A tree, a life, a bench', 'A tree, a fence, a yard'))