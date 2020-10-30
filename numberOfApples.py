n=int(input())
x=list()
y=list()
temp=list()
nop=dict()
flag=0
for i in range(n):
    a,b=input().split()
    x.append(int(a))
    temp.append(int(a))
    if(int(a) in nop):
        nop[int(a)].append(int(b))
    else:
        nop[int(a)]=[int(b)]

temp.sort()
for i in range(n):
    k=x[i]
    ans=0
    flag=0
    for k1 in temp:
        if(k1<k):
            ans+=1
            if(flag==0):
                flag=1
            else:
                flag=0
            continue
        break
    z=nop[k]
    z1=z[:]
    if(flag==1):
        z1.sort(reverse=True)
    else:
        z1.sort()
    for j in z1:
        if(flag==1):
            if(j>z[0]):
                ans+=1
                continue
        if(flag==0):
            if(j<z[0]):
                ans+=1
                continue
        break
    nop[k].append(z[0])
    nop[k].pop(0)
    print(ans)
    
