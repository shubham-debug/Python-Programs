#operation on tuple
#codechef problem june long challenge 2020
#i have solved this problem but it is showing runtime erroe in codechef
#but here in my computer it is not showing any error
#and also when i checked the solution i found that my solution is correct

z=int(input())
for i in range(z):
    p=(int(i) for i in input().split())
    t=(int(i) for i in input().split())
    level=0
    l=list(p)
    t=list(t)
    while(l!=t):
        level+=1
        if(level>10):
            break
        a=t[0]-l[0]
        b=t[1]-l[1]
        c=t[2]-l[2]
        a1=t[0]//l[0]
        b1=t[1]//l[1]
        c1=t[2]//l[2]
        if(a==b==c):
            l[0]+=a
            l[1]+=a
            l[2]+=a
        elif(a1==b1==c1 and a1>1):
            l[0]*=a1
            l[1]*=b1
            l[2]*=c1
        elif(a==b and a!=0):
            l[0]+=a
            l[1]+=a
        elif(b==c and b!=0):
            l[1]+=b
            l[2]+=c
        elif(a==c and c!=0):
            l[0]+=a
            l[2]+=c
        elif(a1==b1 and a1>1):
            l[0]*=a1
            l[1]*=a1
        elif(b1==c1 and b1>1):
            l[1]*=b1
            l[2]*=c1
        elif(a1==c1 and a1>1):
            l[0]*=a1
            l[2]*=c1
        elif(a!=0):
            l[0]+=a
        elif(b!=0):
            l[1]+=b
        elif(c!=0):
            l[2]+=c
        elif(a1>1):
            l[0]*=a1
        elif(b1>1):
            l[1]*=b1
        elif(c1>1):
            l[2]*=c1
        #print(l)

    print(level)
            
            
        

