#this is kruskal algorithm
#here I am going to use the inbuilt set(hash table) present in python
#lets see what happens
#the graph is going to be in the form of dictionary
#but I am going to implement it in the linked list i.e:adjacency list form too
def findSet(parent,i):
    if(parent[i]!=i):
        parent[i]=findSet(parent,parent[i])
    return parent[i]


def unionSet(parent,rank,i,j):
    u=findSet(parent,i)
    v=findSet(parent,j)
    if(rank[u]>rank[v]):
        parent[v]=u
    else:
        parent[u]=v
        if(rank[u]==rank[v]):
            rank[v]+=1
            


def kruskal(graph):
    parent=dict()
    rank=dict()
    for i in graph:
        parent[i]=i
        rank[i]=0
    l=[[i,j[0],j[1]] for i in graph for j in graph[i]]
    l=sorted(l,key=lambda x:x[2])
    #print(l)
    mst=list()
    for i in l:
        if(findSet(parent,i[0])!=findSet(parent,i[1])):
            unionSet(parent,rank,i[0],i[1])
            mst.append(i)
    
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

    print("The minimum spanning tree for the graph is:")
    tree=kruskal(graph)
    for i in tree:
        print('{0}-->{1}={2}'.format(i[0],i[1],i[2]))






    
