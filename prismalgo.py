#prim algorithm
#here the graph is represented as dictionary
#another program for adjacency list will be written tomorrow
def buildheap(q):
    heapsize=len(q)
    for i in range((len(q)//2)-1,-1,-1):
        heapify(q,i,heapsize)



def heapify(q,i,size):
    l=(2*i)+1
    r=(2*i)+2
    if(l<size and q[l][1]<q[i][1]):
        smallest=l
    else:
        smallest=i
    if(r<size and q[r][1]<q[i][1]):
        smallest=r
    if(smallest!=i):
        q[i],q[smallest]=q[smallest],q[i]
        heapify(q,smallest,size)

def extract(q):
    z=q[0]
    q[0],q[-1]=q[-1],q[0]
    q.pop(-1)
    heapify(q,0,len(q))
    
    return(z)

def findwt(graph,u,i):
    for z in graph[u]:
        if(z[0]==i):
            return(z[1])

def updatekey(heap,key,node):
    counter=0
    for i in heap:
        if(i[0]==node):
            i[1]=key
            break
        counter+=1
    while(counter>0 and heap[(counter-1)//2][1]<heap[counter][1]):
        heap[counter],heap[(counter-1)//2]=heap[(counter-1)//2],heap[counter]
        counter=(counter-1)//2
    
        

def prim(graph,key):
    parent=dict()
    wt=dict()
    n=set()
    for i in graph:
        wt[i]=float('inf')
        parent[i]=None
        n.add(i)
    wt[key]=0
    q=[[i,wt[i]] for i in wt]
    buildheap(q)
    while(q):
        u=extract(q)
        n.remove(u[0])
        for i in graph[u[0]]:
            z=findwt(graph,u[0],i[0])
            if(i[0] in n and z<wt[i[0]]):
                parent[i[0]]=u[0]
                wt[i[0]]=z
                updatekey(q,z,i[0])
        heapify(q,0,len(q))
    print(parent)
    return(wt)



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


    print("the minimum spannig tree is")
    print(prim(graph,'a'))
   
