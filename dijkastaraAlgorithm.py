#dijkstra algorithm

#this function does minheapify for a particular index and the approach
#is top down
#time complexity O(lg n)
def minHeapify(heap,i):
    l=2*i+1
    r=2*i+2
    if(l<len(heap) and heap[l][1]<heap[i][1]):
        smallest=l
    else:
        smallest=i
    if(r<len(heap) and heap[r][1]<heap[i][1]):
        smallest=r
    if(smallest!=i):
        heap[i],heap[smallest]=heap[smallest],heap[i]
        minHeapify(heap,smallest)
    return


#this is the function for building the
#min heap form an array given by the user
#time complexity O(n)
def buildMinHeap(arr):
    for i in range(len(arr)//2,-1,-1):
        minHeapify(arr,i)
    return

#this function extract the minimum from the heap
#time complexity O(lg n)
def extractMinNode(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    ans=arr.pop()
    minHeapify(arr,0)
    return ans

#this fuction decrease the key value for a given node
#time complexity O(lg n)
def decreaseKey(arr,i,key):
    arr[i][1]=key
    while(i>0):
        if(arr[(i//2)-1][1]>arr[i][1]):
            arr[(i//2)-1],arr[i]=arr[i],arr[(i//2)-1]
            i=i//2
        else:
            break
    return


#finding the node in the heap
def findNode(arr,i):
    for j in range(len(arr)):
        if(arr[j][0]==i):
            return j


#dijkstara algorithm
#time complexity  O(V + ElgV) which is simply O(ElgV)
def dijkstra(graph,s):
    arr=list()
    for i in graph:
        if(i == s):
            arr.append([i,0])
            continue
        arr.append([i,float('inf')])
    sf=dict()
    #initialize graph
    for i in graph:
        sf[i]=[None,float('inf')]
    sf[s][1]=0
    s=set()
    buildMinHeap(arr)
    while(arr):
        temp=extractMinNode(arr)
        s.add(temp[0])
        for i in graph[temp[0]]:
            if(temp[1]+i[1]<sf[i[0]][1] and i[0] not in s):
                k=findNode(arr,i[0])
                decreaseKey(arr,k,temp[1]+i[1])
                sf[i[0]]=[temp[0],temp[1]+i[1]]            
    return sf
        
        
        
    


#this is the main function
if __name__=="__main__":
    graph=dict()
    vertices=input("Enter the vertices of the graph\n")
    for i in vertices.split():
        graph[int(i)]=list()
    while(True):
        u,v,w=map(int,input("Enter the edge and weight\n").split())
        graph[u].append([v,w])
        if(int(input("Enter 0 to continue\n"))):
            break
    print(graph)
    '''graph={
        's':[['t',10],['y',5]],
        't':[['x',1],['y',2]],
        'y':[['z',2],['x',9],['t',3]],
        'z':[['x',6],['s',7]],
        'x':[['z',4]]
        }'''
    print(dijkstra(graph,0))
        
        






















    
    
