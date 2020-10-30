def seive(n):
    prime=[True for i in range(n+1)]
    for i in range(2,n+1):
        if(prime[i]==True):
            for j in range(i*i,n+1,i):
                prime[j]=False
    pri=list()
    for i in range(2,n+1):
        if(prime[i]):
            pri.append(i)
    return pri



    
n=int(input())
count=0
pri=seive(n)
print(pri)
for i in pri[1:]:
    temp=0
    j=0
    while(True):
        temp+=pri[j]
        if(temp==i):
            count+=1
            break
        elif(temp>i):
            break
        j+=1
    print(temp)
print(count)
