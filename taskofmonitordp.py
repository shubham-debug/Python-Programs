#task of class monitor

def solve(n,k,h):
    tallest=0
    ans=0
    count=dict()
    count[0]=1
    for i in range(n):
        tallest=max(tallest,h[i])
        if(tallest in count):
            count[tallest]+=1
        else:
            count[tallest]=1

    print(count)
    for i in range(n):
        j=i
        tallest=0
        while(j<n):
            tallest=max(tallest,h[j])
            if(abs(tallest-h[i])<=k):
                if(tallest in count):
                    ans+=count[tallest]
                    j+=count[tallest]
                else:
                    ans+=1
                    j+=1
                continue
            break
        
    return ans



if __name__=="__main__":
    n,k=map(int,input().split())
    h=[0]*n
    for i in range(n):
        h[i]=int(input())
    print(solve(n,k,h))
