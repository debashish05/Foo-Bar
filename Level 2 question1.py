def to_base_b(n,b):
    t=""
    while n>=b:
        t+=str(n%b)
        n=n//b
    t+=str(n)
    t=t[::-1]
    return t

def solution(n, b):

    mapping= {}
    count=0
    while n not in mapping:
        
        y=''.join(sorted(n))
        x=y[::-1]
        z=to_base_b(int(x,b)-int(y,b),b)

        temp=""
        if len(z)<len(x):
            for i in range(len(x)-len(z)):
                temp=temp+'0'
        z=temp+z

        mapping[n]=count
        count=count+1
        n=z

    return (count-mapping[n])
