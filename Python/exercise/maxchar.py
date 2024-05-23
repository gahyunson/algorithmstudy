# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

def maxChar1(str):
    dic = {}

    for s in str:
        if s not in dic:
        # if not dic[s]: -> KeyError
            dic[s]=1
        else:
            dic[s]+=1
    
    max_num = 0
    char = ''
    for k in dic:
        if dic[k]>max_num:
            max_num = dic[k]
            char = k 
    return char 


from collections import Counter 

def maxChar2(str):
    chars = Counter(str)
    result = max(chars, key=chars.get) 

    return result


print(maxChar2('11110202020111111'))