def solution(n,a,b):
    answer = 0
    for i in range(1,n+1) :
        if b%2==0 and b-a==1:
            answer=i
            return answer
        a=(a//2+a%2)
        b=(b//2+b%2)