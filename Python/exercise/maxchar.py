# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

'''
I first reated a string dictionary. Then, I searched for the key corresponding to the maximum value in the dictionary.
'''

def maxChar1(str):
    # empty object
    dic = {}

    for s in str:
        # I received every character
        # I'll add an entry to dic.
        if s not in dic:
        # if not dic[s]: -> KeyError
            dic[s]=1
        # if en entry already exists, just add one to the number.
        else:
            dic[s]+=1
    
    # find the character that was used most frequently in a given string.
    max_num = 0 # max set to zero 
    char = '' # char set to an empty string
    for k in dic: 
        # k is assigned the keys inside dic object
        if dic[k]>max_num: # if we ever find a character that has more uses than Max, then we'll set Max equal to that new value
            max_num = dic[k] # max_num become dic at k
            char = k # I'll set char to the character that was responsible for that number of uses.
            # char will become k
    return char 


from collections import Counter 

def maxChar2(str):
    chars = Counter(str)
    result = max(chars, key=chars.get) 

    return result


print(maxChar2('11110202020111111'))