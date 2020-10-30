#given a sorted dictionary of an alien language, find order of characters


def createGraph(arr):
    graph=dict()
    for i in arr:
        for j in i:
            if(j not in graph):
                graph[j]=list()
    for i in range(len(arr)-1):
        temp=arr[i]
        temp1=arr[i+1]
        l=min(len(temp),len(temp1))
        for j in range(l):
            if(temp[j]!=temp1[j]):
                graph[temp[j]].append(temp1[j])
                break
    return graph



def topologicalSort(graph):
    l=list()
    s=set()
    for i in graph:
        if(i not in s):
            s.add(i)
            topologicalSortUtil(graph,i,l,s)
            l.append(i)

    return l[-1::-1]

def topologicalSortUtil(graph,i,l,s):
    for j in graph[i]:
        if(j not in s):
            s.add(j)
            topologicalSortUtil(graph,j,l,s)
            l.append(j)


                       
if __name__=="__main__":
    arr=[i for i in input().split()]
    graph=createGraph(arr)
    print(graph)
    print(topologicalSort(graph))
