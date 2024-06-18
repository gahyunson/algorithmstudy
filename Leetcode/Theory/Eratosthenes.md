# Sieve of Eratosthenes 

To find all primes number(소수) under N

How? filter multiple(배수) of the prime number.

Example. N = 50,  
Below is filter sequece
1. 1
2. multiple of 2 , except 2
3. multiple of 3 , except 3
4. 4 is already filtered
5. multiple of 5 , except 5
6. multiple of 6 , except 6 (but already filtered)
7. keep going ... to 50

- O(NlogN)


```python
# O(n*log(log(n)))
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    # start at 'num = 2'
    p = 2
    while p*p <= num:
        if prime[p]:
            for i in range(p*p, num+1, p):
                prime[i] = False 
        p += 1
    
    # print 
    for p in range(2, num+1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    SieveOfEratosthenes(30)
```