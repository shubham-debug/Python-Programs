#number of divisior


def solve(a,b):
    ans=a//2
    ans*=(1+a)
    n=a//b
    ans1=n*(2*b+(n-1)*b)//2
    ans-=ans1
    l=list()
    j=0
    for i in range(1,n+1,1):
        if(i%b==0):
            l.append(l[j])
            j+=1
            ans+=l[i-1]
            continue
        l.append(i)
        ans+=l[i-1]
    print(ans)
        

    
    





if __name__=="__main__":
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        solve(a,b)
