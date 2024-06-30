# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'

'''
It wants to apitalize the first letter of each word in the string then return the capitalized string.

How to approach?
1. Check each characters of the string and capitalize the first letter of the string following any space.
2. Split the string by space, then replacing the first character of the substring to a character capitalized.
3. split the string by space and then capitalizing s the first character of the substring.

1. 문자열의 캐릭터 하나씩 다 점검을 해서 공백이 있으면 공백 후의 단어를 대문자로 바꾸는 방법
2. 문자열을 공백 기준으로 나눈 다음 각 부분 배열의 가장 첫번째 인덱스 값을 추출해서 대문자로 바꾸는 방법
3. 문자열을 공백 기준으로 나누어 배열을 만든 다음, 각 부분배열의 첫번째(0) 인덱스 값을 대문자로 대체하는 방법
'''

# string append , string upper method
def capitalize(str):
    # create 'result' which is the first character of the input string capitalized
    result = str[0].upper()

    # For each character in the string
    for i in range(1, len(str)):
        # if the character to the left a space
        if str[i-1] == ' ':
            # capitalize it and add it to 'result'
            result = result + str[i].upper()
        else:
            # add it to result
            result = result + str[i]
    return result

# list append
def capitalize2(str):
    # make an empty array 'result'
    result = []
    # split the input string by spaces to get an array
    # For each word in the array
    for word in str.split(' '):
        # uppercase the first letter of the word 
        # join first letter with rest of the string
        # append result into 'result' array
        result.append(word[0].upper() + word[1:])
    # join result into a string and return it
    return ' '.join(result)

def capitalize3(str):
    # Split the input string.
    strArr = str.split()
    # make an empty array
    result = []

    # check substring of the string
    for str in strArr:
        # replace the first character of substring to capitalized
        # add substring replaced to result
        result.append(str.replace(str[0], str[0].upper()))
    # join result into a string and return it
    return ' '.join(result)


print(capitalize2('hi there, how is it going?'))
print(capitalize2('i love breakfast at bill miller bbq'))
print(capitalize2('look, it is working!'))