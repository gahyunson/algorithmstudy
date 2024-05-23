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

print(anagrams1('Hello!!', 'elhlo'))