#lcm of array of elements modulo m

def seive():
    arr=[True for i in range(100000)]
    arr[0],arr[1]=False,False
    for i in range(2,len(arr)):
        if(arr[i]):
            for j in range(i*i,len(arr),i):
                arr[j]=False
    prime=list()
    for i in range(len(arr)):
        if(arr[i]):
            prime.append(i)
    return prime

def factor(i,z):
    ans=0
    while(i%z==0):
        ans+=1
        i=i//z
    return ans,i


def power(i,pure,prime):
    counter=0
    while(i>1):
        print(pure)
        if(i%prime[counter]==0):
            z,i=factor(i,prime[counter])
            if(prime[counter] in pure and z>pure[prime[counter]]):
                pure[prime[counter]]=z
            elif(prime[counter] not in pure):
                pure[prime[counter]]=z
        counter+=1
    

def solve(n,m,k,arr,prime):
    pure=dict()
    for i in arr:
        power(i,pure,prime)
    ans=1
    for i in pure:
        ans*=i**pure[i]
    ans=ans**k
    return ans%m
        
        


if __name__=="__main__":
    t=int(input())
    prime=seive()
    for test in range(t):
        n,m,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        print(solve(n,m,k,arr,prime))
    


