#chef and frogs code chef easy





n,k,p=list(map(int,input().split()))
lx=[int(i) for i in input().split()]
gx=lx[:]
gx.sort()
pair=list()
for i in range(p):
    pair.append(tuple(list(map(int,input().split()))))
for a,b in pair:
    z=gx.index(lx[a-1])
    z2=gx.index(lx[b-1])
    for i in range(z,z2,1):
        if(gx[i]-gx[i+1]<=k and gx[i]-gx[i+1]>=-k ):
            continue
        print('No')
        break
    else:
        print('Yes')
        
