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