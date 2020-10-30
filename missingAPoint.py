#missing a point
#just do the xor operation
#in the name of god the almighty

def solve(arr):
    ans=arr[0]
    for i in range(1,len(arr)):
        ans=ans ^ arr[i]
    return ans

    
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        x=list()
        y=list()
        n=int(input())
        for j in range((4*n)-1):
            a,b=map(int,input().split())
            x.append(a)
            y.append(b)
        x1=solve(x)
        y1=solve(y)
        print(x1,y1)
        
