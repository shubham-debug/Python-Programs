#maxmex

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=[int(j) for j in input().split()]
    p=sorted(a)
    k=set(a)
    if(m<=p[0]):
        print(len(a))
        continue
    if(m>p[-1]):
        print('-1')
        continue
    counter=0
    stor=0
    for i in a:
        if(i < m):
            counter+=1
            stor=i
            continue
        if(i
            
    print(counter)
    
        
