#Special numbers(Hackerearth august easy)

def gcd(x,y):
    temp=y%x
    if(temp==0):
        return x
    return gcd(temp,x)


def findNumber():
    s=[4,7]
    l=s[:]
    for i in range(9):
        n=list()
        for j in s:
            n.append(j*10+4)
            l.append(j*10+4)
            n.append(j*10+7)
            l.append(j*10+7)
        s=n
    return l
    
    

if __name__=="__main__":
    n=int(input())
    p=findNumber()
    ans=0
    k=list()
    for i in p:
        if(i<=n):
            k.append(i)
        else:
            break
    print(k)
    for i in range(len(k)):
        for j in range(i,len(k)):
            if(gcd(k[i],k[j])==1):
                ans+=1
    print(ans)
        
    
