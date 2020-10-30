#task of class monitor

def solve(n,k,h):
    tallest=0
    ans=0
    for i in range(n):
        for j in range(i,n):
            tallest=max(tallest,h[j])
            if(abs(tallest-h[i])<=k):
                ans+=1
                continue
            break
    return ans



if __name__=="__main__":
    n,k=map(int,input().split())
    h=[0]*n
    for i in range(n):
        h[i]=int(input())

    print(solve(n,k,h))
