import math

def solution(n):
    
    n=int(n)
    base=[0,0,1,2,2]    #values of base cases where n=0,1,2,3,4

    count=0    
    while n>4 :
        while n&1==0 and n>4:
            n>>=1
            count+=1

        if(n<=4):
            return count+base[n]

        if (n-1)&1==0 and ((n-1)>>1)&1==0:      #divisible by 4
            n=n-1
        else :
            n=n+1
        count+=1

    return count+base[n]

print(solution(str(15)))