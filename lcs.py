#Longest common subsequence problem
#so now i will only print the length of longest common subsequence
#not the subsequence
#so it is easy


def bruteForcee(a,b,lcs):
    if((not len(a)) or (not len(b))):
        return lcs
    for i in range(len(b)):
        temp = 0
        for j in range(len(a)):
            if(b[i] == a[j]):
                temp += 1 + bruteForcee(a[j+1:],b[i+1:],temp)
                break
        lcs = max(lcs,temp)
    return lcs


def bruteForce(a,b,s):
    if((not len(a)) or (not len(b))):
        return s
    for i in range(len(b)):
        temp = ''
        for j in range(len(a)):
            if(b[i] == a[j]):
                temp += b[i] + bruteForce(a[j+1:],b[i+1:],temp[:])
                break
        if(len(s)<len(temp)):
            s = temp[:]
    return s

#bottom up dp(and i don't know how to do it so it may take some time and reading
#so to understand it and be clear about how dp works in 2D)
#then lets make it.
def bottomUp(a,b):
    dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if(b[j-1]==a[i-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[-1][-1]





if __name__=="__main__":
    a=input()
    b=input()
    #z=bruteForce(a,b,'')
    #k = bruteForcee(a,b,0)
    #print(z)
    #print(k)
    z = bottomUp(a,b)
    print(z)



    
