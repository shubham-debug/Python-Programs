#0/1 knapsack problem dp

def knapsack(n,wt,val,sack):
    dp=[[0 for i in range(sack+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(sack+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(wt[i-1]<=j):
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]


if __name__=="__main__":
    n=int(input("Enter the number of elements\n"))
    wt=[int(i) for i in input("Enter the weight\n").split()]
    val=[int(i) for i in input("Enter the value\n").split()]
    sack=int(input("Enter the sack value\n"))
    print(knapsack(n,wt,val,sack))
