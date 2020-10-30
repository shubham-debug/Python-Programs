#chef and dragon dens
#codechef

def solve(height,taste,a,b,c):
    if(height[c-1]>=height[b-1]):
        return -1
    if(b>c):
        counter=-1
    else:
        counter=1
    if(counter==-1):
        real=height[c-1:b]
    else:
        real=height[b-1:c]
    real=list(set(real))
    ans=taste[b-1]
    z=b+counter-1
    temp=height[b-1]
    real.sort()
    if(real[-1]!=height[b-1]):
        return -1
    real.pop()
    while(z!=c-1):
        if(not len(real)):
            break
        if(height[z]==real[-1]):
            real.pop()
            ans+=taste[z]
        z+=counter
    ans+=taste[c-1]
    return ans
    

if __name__=="__main__":
    n,q=map(int,input().split())
    height=[int(i) for i in input().split()]
    taste=[int(i) for i in input().split()]
    for i in range(q):
        a,b,c=map(int,input().split())
        if(a==1):
            taste[b-1]=c
        else:
            print(solve(height,taste,a,b,c))
            
    
