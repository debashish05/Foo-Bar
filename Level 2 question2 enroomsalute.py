def solution(s):
    # Your code here
    ans=0
    count=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='<':
            count=count+1
        elif s[i]=='>':
            ans+=count
    return 2*ans
