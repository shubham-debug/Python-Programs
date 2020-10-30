#chef and the string

def solve(arr,n):
    ans=0
    for i in range(1,n):
        ans+=abs(arr[i-1]-arr[i])-1
    return ans





    

if __name__=="__main__":
    t=int(input())
    for j in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        print(solve(arr,n))
