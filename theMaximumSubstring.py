from collections import Counter 
st=input()
bis=Counter(st)
lis=[]
m=max(bis.values())
for i in bis:
    if bis[i]==m:
        lis.append(i)
sam="".join(lis)
#print(sam)
s=sam[0]
print(sam[0:m+1])
