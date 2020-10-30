#finding k cores


def solve(graph,j):
    temp=dict()
    for i in graph:
        temp[i]=len(graph[i])
    while(True):
        flag=True
        for i in graph:
            if(i in temp and temp[i]<j):
                flag=False
                deleteDegree(graph,i,temp)
                temp.pop(i)
        if(flag):
            break
    ans=dict()
    for i in temp:
        ans[i]=list()
        for j in graph[i]:
            if(j in temp):
                ans[i].append(j)
    return ans


def deleteDegree(graph,i,temp):
    for j in graph[i]:
        if(j in temp):
            temp[j]-=1

        

if __name__=="__main__":
    graph={0: [1, 2], 1: [0, 2, 5], 2: [0, 1, 3, 4, 5, 6],
           5: [1, 2, 6, 8], 3: [2, 4, 6, 7], 4: [2, 3, 6, 7],
           6: [2, 3, 4, 5, 7, 8], 7: [3, 4, 6], 8: [5, 6]}
    print(solve(graph,3))
