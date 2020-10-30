#the maximum number
def solve(n,i,arr):
    arr.sort()
    mx=float('-inf')
    ans=0
    l=list()
    t=arr[-1]
    pu=0
    while(t>0):
        t=t//2
        pu+=1
    if(pu<i):
        return -1
    
    for j in range(arr[-1],-1,-1):
        if(bin(j).count('1')==i):
            key=0
            for k in arr:
                key+=k & j
            l.append(key)
            mx=max(mx,key)
    ans=l.count(mx)
    return ans
                

if __name__=="__main__":
    t=int(input())
    for j in range(t):
        n,i=map(int,input().split())
        arr=[int(p) for p in input().split()]
        print(solve(n,i,arr))
