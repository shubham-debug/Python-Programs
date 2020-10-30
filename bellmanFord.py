#the bellman ford algorithm
#single source shortest path
#this uses dynamic programming
#graph is given in dictionary
def initailize(graph,s):
    sp=dict()
    for i in graph:
        sp[i]=[float('inf'),None]
    sp[s]=[0,None]
    return sp
      

def relax(u,v,w,sp):
    if(sp[u][0]>sp[v][0]+w):
        sp[u][0]=sp[v][0]+w
        sp[u][1]=v


def bellmanford(graph,s):
    sp=initailize(graph,s)
    for i in range(len(graph)-1):
        for j in graph:
            for p in graph[j]:
                relax(p[0],j,p[1],sp)
    for j in graph:
        for p in graph[j]:
            if(sp[p[0]][0]>sp[j[0]][0]+p[1]):
                return False
    return sp
    
    
        


if __name__=="__main__":
    graph={'s': [['t', 6], ['y', 7]], 't': [['x', 5], ['z', -4], ['y', 8]], 'x': [['t', -2]], 'y': [['z', 9], ['x', -3]], 'z': [['x', 7], ['s', 2]]}

    '''vertex=input("Enter the name of the vertex\n")
    for i in vertex.split():
        graph[i]=list()

    while(True):
        u,v,w=input("Enter the edge and weight\n").split()
        graph[u].append([v,int(w)])
        if(int(input("Enter 0 to continue\n"))):
           break

    print(graph)'''
    print(bellmanford(graph,'s'))
