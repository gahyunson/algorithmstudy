# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'

# string append , string upper method
def capitalize(str):
    result = str[0].upper()

    for i in range(1, len(str)):
        if str[i-1] == ' ':
            result = result + str[i].upper()
        else:
            result = result + str[i]
    return result

# list append
def capitalize2(str):
    result = []
    for word in str.split(' '):
        result.append(word[0].upper() + word[1:])
    return ' '.join(result)

def capitalize1(str):
    strArr = str.split()
    result = []

    for str in strArr:
        result.append(str.replace(str[0], str[0].upper()))
    return ' '.join(result)


print(capitalize2('hi there, how is it going?'))
print(capitalize2('i love breakfast at bill miller bbq'))
print(capitalize2('look, it is working!'))