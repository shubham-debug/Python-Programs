#answer of the question
def lcd(l,i):
    n=1
    for j in l[1:]:
        if(i%j==0):
            n=i//j
            break
    return n

def soe(n):
    prime=[True for i in range(n+1)]
    p=2
    l=[1]
    while(p*p<=n):
        if(prime[p]==True):
            l.append(p)
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    return l


def solve(temp,l,r):
    if(l==1):
        n=1
    else:
        n=temp[l-1]
        
    ans=temp[r-1]//n
    k=10**9
    k+=7
    return ans%k
    


if __name__=="__main__":
    n=int(input())
    arr=[int(i) for i in input().split()]
    q=int(input())
    l=soe(10**3)
    #dnc=dict()
    #for i in arr:
        #if(i in dnc):
            #continue
        #else:
            #dnc[i]=lcd(l,i)
    #print(dnc)
    prev=1
    counter=0
    for i in arr:
        prev*=lcd(l,i)
        arr[counter]=prev
        counter+=1
    #print(temp)
    for i in range(q):
        l,r=map(int,input().split())
        print(solve(arr,l,r))





        
