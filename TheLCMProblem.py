#the lcm problem
#not able to solve under time constraint

def gcd(a,b):
    num=b
    den=a
    rem=num%a
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    return den


def lcm(m,n):
    l=m
    for j in range(m+1,n+1):
        mi=min(l,j)
        ma=max(l,j)
        gcdd=gcd(mi,ma)
        l=(j*l)//gcdd
    return(l)

def lcmm(a,b):
    return (a*b)//gcd(a,b)

n=int(input())
lc=lcm(1,n)

m=n//2+1
for i in range((n//2)+1,n+1):
    if(lcm(i,n)!=lc):
        break
    m=i


print(m)

    
            

