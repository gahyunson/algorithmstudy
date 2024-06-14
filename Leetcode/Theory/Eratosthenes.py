# O(n*log(log(n)))
def SieveOfEratosthenes(num):
    # range : 0 ~ num+1 -> 후에 2 ~ num+1 범위로 수정할 것
    prime = [True for i in range(num+1)]

    # start at 'num = 2'
    p = 2
    while p*p <= num:
        if prime[p]:
            for i in range(p*p, num+1, p):
                # 2*2 ~ 50 , 2배수마다
                # 3*3 ~ 50 , 3배수마다
                prime[i] = False 
        p += 1
    
    # print 
    for p in range(2, num+1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    SieveOfEratosthenes(50)