#hexadecimal numbers
import math

def gcd2(x,y):
    ans=0
    n=min(x,y)
    if(x==y!=1):
        return True
    for i in range(2,n+1):
        if(x%i==0 and y%i==0):
            return True
    return False

def gcd1(x,y):
    a=min(x,y)
    b=max(x,y)
    while(a):
        c=b
        b=a
        a=c%a
    return b
        
        
        
        

def solve(l,r):
    ans=0
    for i in range(l,r+1):
        fx=hex(i)
        fx=fx[2:]
        f=0
        for j in fx:
            if(j=='a'):
                f+=10
            elif(j=='b'):
                f+=11
            elif(j=='c'):
                f+=12
            elif(j=='d'):
                f+=13
            elif(j=='e'):
                f+=14
            elif(j=='f'):
                f+=15
            else:
                f+=int(j)
        if(gcd1(i,f)>1):
            ans+=1
    return ans



        



if __name__=="__main__":
    t=int(input())
    for i in range(t):
        l,r=map(int,input().split())
        print(solve(l,r))            
