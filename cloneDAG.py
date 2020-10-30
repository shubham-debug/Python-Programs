#clone a dag
#graph is in the form of adjacency list
#linked list format

class Node:
    def __init__(self,key):
        self.key=key
        self.next=None



class Vertex:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.edge=None


class Graph:
    def __init__(self):
        self.graph=None

    def addVertex(self,vertex):
        if(self.graph==None):
            self.graph=Vertex(vertex)
        else:
            temp=self.graph
            while(temp.next):
                temp=temp.next
            temp.next=Vertex(vertex)

    def addEdge(self,src,dest):
        temp=self.graph
        while(temp):
            if(temp.key==src):
                break
            temp=temp.next
        else:
            return
        temp1=temp.edge
        if(temp1==None):
            temp.edge=Node(dest)
        else:
            while(temp1.next):
                temp1=temp1.next
            temp1.next=Node(dest)
            
    

    def printGraph(self):
        temp=self.graph
        while(temp):
            print(temp.key,end='')
            temp1=temp.edge
            while(temp1):
                print('->',temp1.key,end='')
                temp1=temp1.next
            print()
            temp=temp.next

def clone(g):
    cg=Graph()
    temp=g.graph
    while(temp):
        cg.addVertex(temp.key)
        cloneUtil(cg,temp)
        temp=temp.next
    return cg

def cloneUtil(cg,temp):
    temp1=temp.edge
    while(temp1):
        cg.addEdge(temp.key,temp1.key)
        temp1=temp1.next
            
            
        



if __name__=="__main__":
    g=Graph()
    while(True):
        g.addVertex(input('Enter vertex of graph\n'))
        if(int(input('Enter 0 to continue\n'))):
            break
    while(True):
        a,b=input('Enter vertex of src and dest\n').split()
        g.addEdge(a,b)
        if(int(input('Enter 0 to continue\n'))):
            break
    g.printGraph()
    cg=clone(g)
    cg.printGraph()
    
    



    


