#kosaraju's algorithm for strognly connected components
#time complexity O(E+V)
#the approach do a dfs and store all the vertices in a stack which finishes
#then transpose the graph
#then pop elements one by one and do dfs util on that 


def stronglyConnected(graph):
    stack=list()
    dfs(graph,stack)
    antigraph=transposeGraph(graph)
    #print(antigraph)
    stronglyconnected=list()
    #print(stack)
    visit=set()
    while(stack):
        u=stack.pop()
        if(u not in visit):
            st=list()
            visit.add(u)
            stronglyconnected.append(dfsUtil(antigraph,u,visit,st))
    return stronglyconnected
        


def transposeGraph(graph):
    antigraph=dict()
    for i in graph:
        antigraph[i]=list()
    for i in graph:
        for j in graph[i]:
            antigraph[j].append(i)
    return antigraph


def dfs(graph,stack):
    visited=set()
    for i in graph:
        if(i not in visited):
            visited.add(i)
            dfsUtil(graph,i,visited,stack)


def dfsUtil(graph,i,visited,stack):
    for j in graph[i]:
        if(j not in visited):
            visited.add(j)
            dfsUtil(graph,j,visited,stack)
    stack.append(i)
    return stack
            



if __name__=="__main__":
    graph=dict()
    for i in input("Enter the vertices of the graph\n").split():
        graph[i]=list()
    while(True):
        u,v=input("Enter the edge\n").split()
        graph[u].append(v)
        if(int(input("Enter 0 to continue\n"))):
            break
    print(graph)
    #graph={'3': ['4'], '0': ['2', '3'], '1': ['0'], '4': [], '2': ['1']}
    print(stronglyConnected(graph))
