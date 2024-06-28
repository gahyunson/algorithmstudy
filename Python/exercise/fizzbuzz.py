# Don't try be fancy.

# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# “fizz” instead of the number and for the multiples
# of five print “buzz”. For numbers which are multiples
# of both three and five print “fizzbuzz”.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz

# for문을 이용해서 1부터 n범위의 숫자들이 출력되게 하고,
# 특정 배수들의 경우 특정 문구가 출력되도록 if문을 이용했습니다.
# I printed numbers of range 1 to n with for loop,
# and I changed number to a word at specific numbers with if statement.
def fizzBuzz(n):
    for i in range(1,n+1):
        # Is the number a multiple of 3 and 5?
        if i%3==0 and i%5==0:
            print('fizzbuzz')
            # and I don't want to excute any other code inside the for loop.
        # Is the number a multiple of 5?
        elif i%5==0:
            print('buzz')
        # Is the number a multiple of 3?
        elif i%3==0:
            print('fizz')
        # if it's not a multiple of 15, 5 and 3,
        # just print out the number
        else:
            print(i)

fizzBuzz(15)