#operation on arrays
import time


def choose(tempa,tempb,a,b):
    maxa=a
    maxb=b
    for i in tempa:
        maxa=max(maxa,i^a)
    for i in tempb:
        maxb=max(maxb,i^b)
    return maxa,maxb
        





n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
tempa=list()
tempb=list()
start_time=time.time()
for i in range(len(a)):
    x,y=choose(tempa,tempb,a[i],b[i])
    if(x==y):
        continue
    if(x>y):
        tempb.append(b[i])
    else:
        tempa.append(a[i])
print(len(tempb))
print(time.time()-start_time)
