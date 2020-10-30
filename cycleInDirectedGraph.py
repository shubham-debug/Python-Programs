#detect cycle in directed graph
#simple dfs
#time complexity O(E+V)
#space complexity O(V) this is the stack we use to keep track of edges that
# are currently in recursion stack

#this is a boolean function which return True or False
def graphCycle(graph):
    s=set()
    #stack=set()
    for i in graph:
        stack=set()
        if(i not in s):
            s.add(i)
            stack.add(i)
            k=graphCycleUtil(graph,i,stack,s)
            if(k):
                return True
    return False




def graphCycleUtil(graph,v,stack,s):
    for i in graph[v]:
        if(i not in s):
            s.add(i)
            stack.add(i)
            k=graphCycleUtil(graph,i,stack,s)
            if(k):
                return True
            stack.remove(i)
        elif(i in stack):
            return True
    return False
        




if __name__=="__main__":
    graph={

           1:[2,4,5],
           2:[4,3,9],
           3:[4,6],
           4:[6],
           5:[4],
           6:[],
           7:[9,2],
           8:[7,2],
           9:[]


        
        }
    print(graphCycle(graph))



