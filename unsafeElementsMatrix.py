#unsafe elements in a matrix

def solve(arr,n,m):
    mn=float('inf')
    mx=float('-inf')
    for i in arr:
        for j in i:
            if(j<mn):
                mn=j
            if(j>mx):
                mx=j
    ans=m*n
    p=set()
    z=set()
    for i in range(n):
        for j in range(m):
            if(arr[i][j]==mn or arr[i][j]==mx):
                p.add(i)
                z.add(j)
    print(p)
    print(z)
    ans1=len(p)*m
    ans1+=len(z)*n
    ans1-=len(z)*len(p)
    return ans-ans1
                
                


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n,m=map(int,input().split())
        arr=list()
        for j in range(n):
            arr.append([int(k) for k in input().split()])
        print(solve(arr,n,m))
