#danny password



n=int(input())
l=set()
for i in range(n):
    z=input()
    l.add(z)


for i in l:
    if(i[-1::-1] in l):
        k=len(i)
        z=k//2
        print(k,i[z])
        break
        
    
