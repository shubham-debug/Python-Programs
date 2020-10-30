#path from isengard to middle earth
#this is solved using dynamic programming approach


def solve(a,b,c,d):
    try:
        dp1=[0 for i in range(len(a))]
        dp2=[0 for i in range(len(a))]
        dp1[0]=a[0]
        dp2[0]=b[0]
        for i in range(1,len(a)):
            dp1[i]=min(dp1[i-1],dp2[i-1]+d[i-1])+a[i]
            dp2[i]=min(dp2[i-1],dp1[i-1]+c[i-1])+b[i]
        return min(dp1[-1],dp2[-1])
    except:
        return





    



if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        first=[int(j) for j in input().split()]
        second=[int(j) for j in input().split()]
        if(n>1):
            change1=[int(j) for j in input().split()]
            change2=[int(j) for j in input().split()]
            print(solve(first,second,change1,change2))
        else:
            print(min(first[-1],second[-1]))
