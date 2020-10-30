#number of shelfes


d=dict()
ans=0
t=int(input())
for i in range(t):
    s=input()
    if(s[0] not in d):
        d[s[0]]=1
    else:
        d[s[0]]+=1

for i in d:
    ans+=1
    if(d[i]>10):
        ans+=d[i]//10

print(ans)
