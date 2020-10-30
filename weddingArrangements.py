#chef and wedding arrangements

def solve(n,k,arr):
    dp=[[k if(i==0) else 1 for i in range(len(arr)+1)]for j in range(len(arr))]
    m=float('inf')
    for i in range(len(arr)):
        s=set()
        temp=set()
        count=i
        for j in range(len(arr)):
            if(arr[j] not in  s):
                dp[i][j+1]=dp[i][j]
                s.add(arr[j])
            elif(count>0):
                temp=set()
                s={arr[j]}
                dp[i][j+1]=dp[i][j]+k
                count-=1
            else:
                if(arr[j] not in temp):
                    dp[i][j+1]=dp[i][j]+2
                    temp.add(arr[j])
                else:
                    dp[i][j+1]=dp[i][j]+1
        m=min(m,dp[i][len(arr)])
    #for i in dp:
    #print(i)
    return m


if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        print(solve(n,k,arr))
