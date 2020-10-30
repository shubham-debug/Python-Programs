#minimum cost of the subsequence
#not solved to be continue

def solve(k,a):
    z=list()
    b=sorted(a)
    b=b[:k]
    b=set(b)
    counter=0
    for i in a:
        if(i in b and counter<k):
            counter+=1
            z.append(i)
    odd=-9999999999
    even=-99999999999
    print(z)
    for i in range(k):
        if(i%2==0):
            odd=max(odd,z[i])
        else:
            even=max(even,z[i])
    return(min(odd,even))
    
    
        












if __name__=="__main__":
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    print(solve(k,a))
