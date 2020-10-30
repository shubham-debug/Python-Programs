#maximum gcd

def gcd(n):
    ans=1
    i=2
    while(i*i<=n):
        if(n%i==0):
            ans=n//i
            break
        i+=1
    return ans


def solve(n):
    ans=0
    for i in range(n,0,-1):
        k=gcd(i)
        ans=max(ans,k)
        if(ans==(i//2)):
            break
    return ans
    

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(solve(n))
