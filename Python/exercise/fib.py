# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3
import json
def memoize(fn):
    cache = {}
    def memoized_fn(*args):
        key =  json.dumps(args)
        if key in cache:
            return cache[key]
        result = fn(*args)
        cache[key] = result 
        return result 
    return memoized_fn
def slowFib(n):
    if n<2 :
        return n
    return fib(n-1) + fib(n-2)
fib = memoize(slowFib)


def fib2(n):
    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)

def fib1(n):
    basic = [0, 1]

    if n < 2:
        return basic[n]
    
    '''for i in range(n-1):
        basic.append(basic[i] + basic[i+1])'''
    for i in range(2, n+1):
        basic.append(basic[i-1] + basic[i-2])
    
    return basic[n]

print(fib(4))