#game of strings

a,b=input().split()
ans=0
temp=0
j=0
i=0
counter=0
while(i<len(a) and j<len(b)):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
        i+=1
        temp=0
        counter=i
        j=0
        continue
    if(b[j]=='a' or b[j]=='e' or b[j]=='i' or b[j]=='o' or b[j]=='u' or b[j]=='A' or b[j]=='E' or b[j]=='I' or b[j]=='O' or b[j]=='U'):
        j+=1
        temp=0
    else:
        if(ord(a[i])==ord(b[j])):
            temp+=1
            ans=max(temp,ans)
            i+=1
            j+=1
            counter=i
        else:
            temp=0
            i+=1
            if(i==len(a)):
                i=counter
                j+=1
print(ans)
