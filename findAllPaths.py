#count all possible paths between two vertices
#approach dfs(backtracking)
count=0

def findAllPaths(graph,u,v,visited,l):
    for i in graph[u]:
        if(i not in visited):
            l.append(i)
            visited.add(i)
            if(i == v):
                print(l)
                global count
                count+=1
            else:
                findAllPaths(graph,i,v,visited,l)
        visited.remove(i)
        l.pop()
    
        



if __name__=="__main__":
    graph={
            'a':['b','e','c'],
            'b':['d','e'],
            'c':['e'],
            'd':['c'],
            'e':[]


        }
    visited={'c'}
    l=['c']
    findAllPaths(graph,'c','a',visited,l)
    print(count)
