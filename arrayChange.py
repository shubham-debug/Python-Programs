#Fredo and Array Update
n=int(input())
ans=0
z=input()
for i in z.split():
    ans+=int(i)

ans=ans//n
ans+=1
print(ans)
