def number(n):
    digits=list()
    if(n<=9):
        l=n-1
    else:
        l=9
    for i in range(l,1,-1):
        while(n%i==0):
            digits.append(i)
            n//=i
    return digits


if __name__=="__main__":
    temp=[1,1,2,1,3,1,4,2]
    n=int(input())
    temp1=number(n)
    ans=0
    s=""
    for i in temp1:
        s+=str(i)
    print(s)
    for i in range(2,int(s)+1):
        z=str(i)
        p=1
        for k in z:
            p*=int(k)
        if(p==n):
            ans+=1
    print(ans)
        
