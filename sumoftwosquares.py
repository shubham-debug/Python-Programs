#difference of two squares

t=int(input())
for i in range(t):
    ans=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        if(j%4==2):
            one=j
            break
    for j in range(r,l-1,-1):
        if(j%4==2):
            two=j
            break
    diff1=two-one
    diff1=diff1//4
    ans=(r-l)-diff1
    
        




        
    print(ans)
