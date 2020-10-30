#number of factors

def factor(k):
    ans=0
    i=1
    while(i*i<=k):
        if(k%i==0):
            ans+=1
            if(k//i!=i):
                ans+=1
        i+=1
    return ans
    
        


def solve(n,k,arr):
    ans=0
    sk=arr[k]
    for i in range(1,n+1):
        if(i==k):
            continue
        ik=arr[i]
        if(ik<sk):
            ans+=1
    return ans
    



if __name__=="__main__":
    t,n=map(int,input().split())
    arr=list()
    for i in range(n+1):
        arr.append(factor(i))
    for i in range(t):
        k=int(input())
        print(solve(n,k,arr))
