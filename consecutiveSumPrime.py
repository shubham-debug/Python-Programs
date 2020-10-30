#consecutive prime sum
def seive(n):
    arr=[True for i in range(n+1)]
    for i in range(2,n+1):
        if(arr[i]==True):
            for j in range(i*i,n+1,i):
                arr[j]=False
    prime=list()
    for i in range(2,n+1):
        if(arr[i]==True):
            prime.append(i)
    return prime
        
def solve(n,prime):
    count=0
    #print(prime)
    for i in range(len(prime)):
        #print(prime[i])
        sm=0
        counter=0
        while(counter<len(prime) and sm<prime[i]):
            sm+=prime[counter]
            counter+=1
        #print(sm)
        if(sm==prime[i]):
            count+=1
    return count-1
    
            
if __name__=="__main__":
    n=int(input())
    prime=seive(n)
    print(solve(n,prime))
    
    
