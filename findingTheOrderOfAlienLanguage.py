#finding the order of the alien language

def createGraph(words):
    graph=dict()
    counter=0
    for i in range(len(words)-1):
        for j in words[i]:
            if(j not in graph):
                graph[j]=list()
            k=words[i+1]
            if(counter<len(k)):
                if(j != k[counter]):
                    graph[j].append(k[counter])
                    counter=float('inf')
                counter+=1

        counter=0
    for i in words[-1]:
        if(i not in graph):
            graph[i]=list()

    return graph
                


def topologicalSort(graph):
    ans=list()
    k=set()
    for i in graph:
        if(i not in k):
            k.add(i)
            topologicalSortUtil(graph,ans,i,k)
            ans.append(i)
    return(ans[-1::-1])




def topologicalSortUtil(graph,ans,i,k):
    for j in graph[i]:
        if(j not in k):
            k.add(j)
            topologicalSortUtil(graph,ans,j,k)
            ans.append(j)
            
            
            
            
            




        


def solve(words):
    graph=createGraph(words)
    return topologicalSort(graph)




 

if __name__=="__main__":
    n=int(input("Enter the number of words\n"))
    words=list()
    for i in range(n):
        words.append(input())

    ans=solve(words)
    for i in ans:
        print(i)
