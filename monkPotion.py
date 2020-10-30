#magic shop potions
#won

a,b=map(int,input().split())
s=input()
ans=0
for i in s:
    if(i=='1'):
        ans+=a
    a=((a%b)*(a%b))%b
print(ans%b)
