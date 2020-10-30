#cersei and her soldiers
#i need to work on it

def solve(n,m,k,d,arr):
    temp=set()
    bo=[True for i in range(len(arr))]
    ans=0
    for i in d:
        if(arr[i-1] not in temp and len(d[i])>1):
            temp.add(arr[i-1])
            ans+=1
            bo[i-1]=False
            for j in d[i]:
                bo[j-1]=False
    for i in bo:
        if(i):
            ans+=1
    
    return ans
            
    


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n,m,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        d=dict()
        for i in range(m):
            u,v=map(int,input().split())
            if(u in d):
                d[u].append(v)
            else:
                d[u]=[v]
        if(len(set(arr))<k):
            print("-1")
        else:
            print(solve(n,m,k,d,arr))
            
