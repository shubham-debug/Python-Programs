#chefina and the chef
#it wants the minimum cost not the minimum number of swaps
#but previously all I was doing is doing the minimum number of swaps
#this is accepted
#in the name of god the almighty

def solve(a,b,n):
    x=dict()
    y=dict()
    ans=0
    for i in range(n):
        if(a[i] not in x):
            x[a[i]]=1
        else:
            x[a[i]]+=1
        if(b[i] not in y):
            y[b[i]]=1
        else:
            y[b[i]]+=1
    actual=min(min(x),min(y))
    p=list()
    q=list()
    for i in x:
        if(i in y):
            if(x[i]==y[i]):
                continue
            elif(abs(x[i]-y[i])%2==0):
                if(x[i]>y[i]):
                    for j in range(abs(x[i]-y[i])//2):
                        p.append(i)
            else:
                return -1
        else:
            if(x[i]%2==0):
                for j in range(x[i]//2):
                    p.append(i)
            else:
                return -1
    for i in y:
        if(i in x):
            if(x[i]==y[i]):
                continue
            elif(abs(x[i]-y[i])%2==0):
                if(y[i]>x[i]):
                    for j in range(abs(x[i]-y[i])//2):
                        q.append(i)
            else:
                return -1
        else:
            if(y[i]%2==0):
                for j in range(y[i]//2):
                    q.append(i)
            else:
                return -1
    if(len(p)==len(q)):
        p=sorted(p)
        q=sorted(q,reverse=True)
        for i in range(len(p)):
            z=min(min(q[i],p[i]),2*actual)
            ans+=z
        return ans
    return -1



if __name__=="__main__":
    t=int(input())
    for z in range(t):
        n=int(input())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        print(solve(a,b,n))
