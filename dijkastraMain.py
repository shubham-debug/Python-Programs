#dijkstra's algorithm for single source shortest path
#in this problem we need min priority queue data structure
#solution

def heapify(arr,i,actual):
    l=(2*i)+1
    r=(2*i)+2
    if(l<len(arr) and arr[l][1]<arr[i][1]):
        smallest=l
    else:
        smallest=i
    if(r<len(arr) and arr[r][1]<arr[smallest][1]):
        smallest=r
    if(smallest!=i):
        actual[arr[smallest][0]]=i
        actual[arr[i][0]]=smallest
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,smallest,actual)

def buildMinHeap(arr,actual):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i,actual)
    return

def extractMin(arr,actual):
    arr[0],arr[-1]=arr[-1],arr[0]
    actual[arr[0][0]]=actual[arr[-1][0]]
    actual[arr[-1][0]]=0
    ans=arr.pop()
    heapify(arr,0,actual)
    return ans

def decreaseKey(arr,actual,key,i):
    arr[i][1]=key
    while(i>0):
        if(i%2==0):
            p=(i//2)-1
        else:
            p=i//2
        if(arr[p][1]>arr[i][1]):
            actual[arr[p][0]]=i
            actual[arr[i][0]]=p
            arr[p],arr[i]=arr[i],arr[p]
            i=p
            continue
        break

def initailizeShortestPath(graph,sp):
    for i in graph:
        sp[i]=[None,float('inf')]
    
#time complexity O(V+ElgV) that is O(ElgV)
def dijkastra(graph,s):
    sp=dict()
    initailizeShortestPath(graph,sp)
    sp[s]=[None,0]
    arr=list()
    for i in sp:
        arr.append([i,sp[i][1]])
    actual=dict()
    for i in range(len(arr)):
        actual[arr[i][0]]=i
    buildMinHeap(arr,actual)
    s=set()
    while(len(arr)):
        z=extractMin(arr,actual)
        s.add(z[0])
        for i in graph[z[0]]:
            if(i[0] not in s and sp[i[0]][1]>i[1]+z[1]):
                sp[i[0]]=[z[0],i[1]+z[1]]
                ind=actual[i[0]]
                decreaseKey(arr,actual,i[1]+z[1],ind)
    return sp
                        
#driver's program
if __name__=="__main__":
    graph={
        's':[['t',10],['y',5]],
        't':[['x',1],['y',2]],
        'y':[['z',2],['x',9],['t',3]],
        'z':[['x',6],['s',7]],
        'x':[['z',4]]
        }
    print(dijkastra(graph,'s'))
    
        
        
