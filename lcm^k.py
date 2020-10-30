import math

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n,m,k=map(int,input().split())
        arr=[int(j) for j in input().split()]
        ans=arr[0]
        for i in range(1,len(arr)):
            if(ans>arr[i]):
                s=arr[i]
                l=ans
            else:
                s=ans
                l=arr[i]
            ans=((arr[i]*ans)//math.gcd(l,s))
        ans=ans**k
        ans%=m
        print(ans)
        
        
