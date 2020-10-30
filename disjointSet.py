#disjoint set operation
#detect cycle in graph
#these two things are to be done here

def makeSet(x,l):
    l[i]=i


def union(x,y,l):
    z=findSet(x,l)
    z1=findSet(y,l)
    if(z!=z1):
        l[z]=z1



def link(x,y,l):
    pass


def findSet(x,l):
    if(l[x]!=x):
        l[x]=findSet(l[x],l)
    return l[x]




if __name__=="__main__":
    n=int(input('Enter the number of vertices\n'))
    l=[-1 for i in range(n)]
    for i in range(n):
        makeSet(i,l)
    print(l)
    while(True):
        x,y=map(int,input('Enter x and y\n').split())
        union(x,y,l)
        print(l)
        if(int(input('Enter 0 to continue\n'))):
            break
    print(findSet(0,l))
    print(l)
