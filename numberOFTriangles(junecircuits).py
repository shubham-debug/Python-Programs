#number of triangles


def solve(n,a,b):
    ans=0
    s=set()
    counter=0
    for i in range(1,n+1):
        if(i!=a and i!=b):
            if(i==n):
                j=1
            else:
                j=i+1
            if(j!=a and j!=b):
                ans+=n-4
                if(i in s):
                    counter-=1
                if(j in s):
                    counter-=1
                s.add(i)
                s.add(j)
    return ans+counter

        

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n,a,b=map(int,input().split())
        print(solve(n,a,b))
