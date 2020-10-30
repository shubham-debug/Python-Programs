#even matrix


def solve(n):
    k=[[0 for i in range(n)] for i in range(n)]
    flag=0
    counter=1
    for i in k:
        if(not flag):
            for j in range(n):
                i[j]=counter
                counter+=1
            flag=1
            continue
        for j in range(n-1,-1,-1):
            i[j]=counter
            counter+=1
        flag=0
    return k

            



if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        k=solve(n)
        for i in k:
            print(*i)
