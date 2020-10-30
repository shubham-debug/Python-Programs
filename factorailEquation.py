#factorial equation hacker-earth may circuits '20


def calc(n):
    if(n<=4):
        ans=1
        for i in range(1,n+1):
            ans*=i
        return ans%10
    return 0



def solve(x,n):
    ans=1
    if(n<=4):
        z=calc(n)
    else:
        print(ans)
        return
    for i in range(z):
        ans=x*ans
    ans=str(ans)
    print(ans[-1])




if __name__=="__main__":
    x,n=map(int,input().split())
    solve(x,n)
