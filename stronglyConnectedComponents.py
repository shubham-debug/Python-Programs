#strongly connected components
#kosaraju algorithm

def transpose(graph):
    graph1=dict()
    for i in graph:
        graph1[i]=list()
    for i in graph:
        for j in graph[i]:
            graph1[j].append(i)
    return graph1


def dfs(graph):
    stack=list()
    z=set()
    for i in graph:
        if(i not in z):
            z.add(i)
            dfsUtil(graph,i,stack,z)
            stack.append(i)
    return stack


def dfsUtil(graph,i,stack,z):
    for j in graph[i]:
        if(j not in z):
            z.add(j)
            dfsUtil(graph,j,stack,z)
            stack.append(j)

def connected(graph,i,z):
    for j in graph[i]:
        if(j not in z):
            z.add(j)
            print('->',j,end='')
            connected(graph,j,z)
            


def stronglyConnected(graph):
    stack=dfs(graph)
    graph1=transpose(graph)
    z=set()
    print(stack)
    while(stack):
        i=stack.pop()
        if(i not in z):
            z.add(i)
            print(i,end='')
            connected(graph1,i,z)
            print()
        
    




if __name__=="__main__":
    graph={
        3:[4],
        1:[0],
        0:[2,3],
        2:[1],
        4:[]
        }
    #transpose(graph)
    stronglyConnected(graph)
    
