"""Reference :https://stackoverflow.com/questions/5124743/algorithm-
            for-simplifying-decimal-to-fractions"""

import math
def multiplication_of_matrix(a,b):
    
    result=[[0 for i in range(len(b[0]))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j]+=(a[i][k]*b[k][j])

    return result

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def matrix_exponentiation(m,power=1000):

    length=len(m)
    result=[[0 for i in range(length)] for j in range(length)]
    #identity matrix
    
    for i in range(length):
        result[i][i]=1

    while power>0:
        if power&1==1:
            result=multiplication_of_matrix(result,m)
        m=multiplication_of_matrix(m,m)
        power//=2

    return result

def decimal_to_fraction(x, error=0.000001):
    """REference mentioned"""
    if x==0:
        return [0,0]
    if 1 - error < x:
        return [1, 1]

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            return [middle_n, middle_d]

def solution(m):
    
    terminal=[]

    length=len(m)
    for i in range(length):     #converting into probability
        count=0
        for j in range(length):
            count+=m[i][j]
        
        if(count==0):
            m[i][i]+=1
            terminal.append(i)

        if count!=0:    
            for j in range(length):
                m[i][j]/=float(count)

    for i in range(length):         # Traversing matrix
        for j in range(i+1,length):
            temp=m[i][j]
            m[i][j]=m[j][i]
            m[j][i]=temp

    start=[[0 for i in range(1)] for j in range(length)] #starting from s0
    start[0][0]=1
    
    m=matrix_exponentiation(m)
    m=multiplication_of_matrix(m,start)

    upper=[]
    lower=[]

    for i in range(len(m)):
        if i in terminal:
            
            temp=decimal_to_fraction(m[i][0])
            upper.append(temp[0])
            lower.append(temp[1])

    finalvalue=0
    i=0
    
    while lower[i]==0:
        i+=1
    finalvalue=lower[i]
    
    for i in range(len(terminal)):
        if(lower[i]!=0):
            finalvalue=(lower[i]*finalvalue)//gcd(finalvalue,lower[i])

    for i in range(len(terminal)):
        if lower[i]!=0:
            upper[i]*=finalvalue//lower[i]

    upper.append(finalvalue)
    return upper