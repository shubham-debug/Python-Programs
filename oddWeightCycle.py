#how to check if there is a cycle in an undirected graph

def findCycle(graph):
    s=set()
    for i in graph:
        temp=set()
        if(i not in s):
            s.add(i)
            temp.add(i)
            parent=-1
            if(findCycleUtil(s,temp,graph,i,parent)):
                return True
    return False


def findCycleUtil(s,temp,graph,i,parent):
    for j in graph[i]:
        if(j not in s):
            s.add(j)
            temp.add(j)
            parent=i
            if(findCycleUtil(s,temp,graph,j,parent)):
                return True
            temp.remove(j)
        elif(j in temp and j != parent):
            #print(temp)
            return True
    return False
     


if __name__=="__main__":
    graph={

        1:[2,0],
        2:[1,3,0],
        3:[2],
        0:[1,2]

            
        }
    print(findCycle(graph))

















    
    
