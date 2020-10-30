# transpose of a graph where graph is given in adjacency list format

def transpose(d):
    z=dict()
    for i in d:
        z[i]=list()


    for i in d:
        for j in d[i]:
            z[j].append(i)

    return z





if __name__=="__main__":
    d={'a':['b','c'],'b':['c'],'c':['d'],'d':['a']}
    print(d)
    z=transpose(d)
    print(z)
