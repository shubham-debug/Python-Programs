#chefina and swaps
#its is not accepted
#just passed sample test case

def solve(a,b):
    actual=min(min(a),min(b))
    x=dict()
    y=dict()
    ans=0
    temp=list()
    temp1=list()
    for i in range(len(a)):
        if(a[i] in x):
            x[a[i]]+=1
        else:
            x[a[i]]=1
        if(b[i] in y):
            y[b[i]]+=1
        else:
            y[b[i]]=1
    for i in x:
        if(i in y):
            if(x[i]==y[i]):
                continue
            elif(abs(x[i]-y[i])%2==0 and x[i]>y[i]):
                temp.append([i,abs(x[i]-y[i])])
            else:
                return -1
        else:
            if(x[i]%2==0):
                temp.append([i,x[i]])
            else:
                return -1
    for i in y:
        if(i in x):
            if(x[i]==y[i]):
                continue
            elif(abs(x[i]-y[i])%2==0 and y[i]>x[i]):
                temp.append([i,abs(x[i]-y[i])])
            else:
                return -1
        else:
            if(y[i]%2==0):
                temp1.append([i,y[i]])
            else:
                return -1
    temp=sorted(temp,key=lambda x:x[0])
    temp1=sorted(temp1,key=lambda x:x[0])
    etemp=list()
    for i in temp:
        for j in range(i[1]//2):
            etemp.append(i[0])

    etemp1=list()
    for i in temp1:
        for j in range(i[1]//2):
            etemp1.append(i[0])
    print(etemp1)
    print(etemp)
    if(len(etemp)==len(etemp1)):
        for i in range(len(etemp)):
            z=min(etemp[i],etemp1[i])
            z=min(z,2*actual)
            ans+=z
    else:
        return -1
    return ans
    
            

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=[int(j) for j in input().split()]
        b=[int(j) for j in input().split()]
        print(solve(a,b))
