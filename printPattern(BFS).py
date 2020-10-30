r,c,x,y=input().split()
l=[[-1 for j in range(int(c))] for i in range(int(r))]
l[int(x)][int(y)]=0
k=[[int(x),int(y)]]
level=1
nt=list()
while(k):
    for i in k:
        p=[[i[0]+1,i[1]+1],[i[0],i[1]+1],[i[0]-1,i[1]+1],[i[0]-1,i[1]],[i[0]+1,i[1]],[i[0]-1,i[1]-1],[i[0],i[1]-1],[i[0]+1,i[1]-1]]
        for j in p:
            if(j[1]<int(c) and j[1]>=0 and j[0]>=0 and j[0]<int(r)):
                if(l[j[0]][j[1]]==-1):
                    l[j[0]][j[1]]=level
                    nt.append([j[0],j[1]])
    k=nt
    nt=list()
    level+=1

for i in range(int(r)):
    for j in range(int(c)):
        print(l[i][j],end=" ")
    print()



