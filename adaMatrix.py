# Ada Matrix


def solve(matrix,n):
    ans=0
    counter=1
    if(matrix[0][1]==2):
        flag=0
    else:
        flag=1
    for i in range(n):
        if(flag==0):
            if(matrix[0][i]!=counter):
                ans+=1
                flag=1
        else:
            if(matrix[i][0]!=counter):
                ans+=1
                flag=0
        counter+=1
    if(flag==1):
        ans+=1
    return ans

if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        matrix=list()
        for j in range(n):
            temp=[int(i) for i in input().split()]
            matrix.append(temp)
        print(solve(matrix,n))
