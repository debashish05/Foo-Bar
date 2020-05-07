#Reference
#https://en.wikipedia.org/wiki/Partition_(number_theory)
#https://en.wikipedia.org/wiki/Pentagonal_number_theorem
#used formula to calculate the no of unique distant partition of n

import math

def findm(k):       
    #3(m^2)-m-k=0 if we find v=a value of m which satisify this so we returrn (-1)**value
    firstroot=(1+math.sqrt(1+12*k))/6
    if firstroot-int(firstroot)==0:
        return (-1)**firstroot
    secondroot=(1-math.sqrt(1+12*k))/6
    if secondroot-int(secondroot)==0:
        return (-1)**secondroot

    return 0

def solution(n):

    l=[1] #for n=0 base case
    for i in range(1,n+1):

        l.append(findm(i))
              
        gk=1
        k=1             #sereis of +1,-1,+2,-2,...
        counter=0       #for series of +1,-1,+2,-2,...
        
        while i-gk>=0 :

            l[i]+=((-1)**(k-1))*l[i-gk] 

            k*=(-1)
            if(counter%2==1):
                k+=1
            counter+=1
                
            gk=(k*(3*k-1))/2
            gk=int(gk)
      
    return int(l[n]-1)            