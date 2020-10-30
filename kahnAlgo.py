#kahn's algorithem for topological sorting
#graph is in the form of dictionary (adjacency list)

def kahnAlgo(graph):
    #visited=set()
    l=list()
    ans=list()
    count=0
    indegree=dict()
    for i in graph:
        if(i not in indegree):
            indegree[i]=0
        for j in graph[i]:
            if(j in indegree):
                indegree[j]+=1
            else:
                indegree[j]=1
            
    print(indegree)
    for i in indegree:
        if(indegree[i]==0):
            l.append(i)
    while(len(l)):
        z=l.pop(0)
        count+=1
        ans.append(z)
        for i in graph[z]:
            indegree[i]-=1
            if(indegree[i]==0):
                l.append(i)
    print(count)
    return ans
        
            



if __name__=="__main__":
    graph={

        0:[],
        1:[],
        2:[3],
        3:[1],
        4:[1,0],
        5:[0,2]

        }
    print(kahnAlgo(graph))
