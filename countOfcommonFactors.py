#count of common factors
a,b=map(int,input().split())
s=min(a,b)
ans=1
counter=2
while(counter<=s//2+1):
    if(a%counter==0 and b%counter==0):
        ans+=1
    counter+=1
print(ans)
