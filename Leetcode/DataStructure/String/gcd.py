def gcd(a, b):
    result = min(a, b)
    while result:
        # When a / b divide result, 
        # the remainder must be zero for both!
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result 

if __name__=='__main__':
    print(gcd(16, 4))