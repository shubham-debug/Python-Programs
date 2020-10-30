#kruskal mst algo

def makeSet(graph):
    s=dict()
    for i in graph:
        s[i]=i
    return s


def findSet(s,u):
    if(s[u]!=u):
        s[u]=findSet(s,s[u])
    return s[u]

def union(s,u,v):
    z=findSet(s,u)
    z1=findSet(s,v)
    if(z!=z1):
        s[z]=z1
        
    


def mstKruskal(graph):
    s=makeSet(graph)
    l=list()
    for i in graph:
        #print(graph[i])
        for j in graph[i]:
            #print(j)
            l.append([i,j[0],j[1]])
    l=sorted(l,key=lambda x:x[2])
    mst=dict()
    for i in l:
        if(findSet(s,i[0])!=findSet(s,i[1])):
            union(s,i[0],i[1])
            if(i[0] not in mst):
                mst[i[0]]=[i[1]]
            else:
                mst[i[0]].append(i[1])
            if(i[1] not in mst):
                mst[i[1]]=[i[0]]
            else:
                mst[i[1]].append(i[0])
    return mst




if __name__=="__main__":
    graph={'a':[('b',4),('h',8)],
           'b':[('c',8),('h',11)],
           'c':[('b',8),('d',7),('f',4),('i',2)],
           'd':[('c',7),('e',9),('f',14)],
           'e':[('d',9),('f',10)],
           'f':[('e',10),('d',14),('c',4),('g',2)],
           'g':[('f',2),('h',1),('i',6)],
           'h':[('a',8),('g',1),('i',7),('b',11)],
           'i':[('c',2),('g',6),('h',7)]}
    print(mstKruskal(graph))
