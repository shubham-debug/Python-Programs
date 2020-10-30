#print all paths


def solve(graph,s,d,temp,l):
    if(s==d):
        print(l)
        return
    
    for i in graph[s]:
        if(i not in temp):
            temp.add(i)
            l.append(i)
            solve(graph,i,d,temp,l)
            temp.remove(i)
            l.pop()
    
    




if __name__=="__main__":
    graph={0:[3,1,2],
           1:[3],
           2:[1,0],
           3:[]
           }
    temp={2}
    l=[2]
    solve(graph,2,3,temp,l)
