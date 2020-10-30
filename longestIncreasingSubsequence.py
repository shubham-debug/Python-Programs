#this problem is the longest increasing array
#let's do this with lazy sort
#two cases :
#[1,5,3,4,7,6,9]
#[1,5,3,7,9,10]


def solve(arr):
    l=[[] for i in range(len(arr))]
    p=list()
    for i in arr:
        if(not p):
            p.append(i)
            l[0].append((i,-1))
        else:
            for j in range(len(p)):
                if(i>p[j]):
                    temp=j
                    break
            else:
                temp=None
            if(temp==0):
                k=-1
            elif(temp==None):
                k=len(l[len(p)-1])
            else:
                k=len(l[temp-1])
            if(temp!=None):
                p[temp]=i
                l[temp].append((i,k))
            else:
                p.append(i)
                l[len(p)-1].append((i,k))
    return l
                



if __name__=="__main__":
    arr=[int(i) for i in input("Enter the array\n").split()]
    print(solve(arr))
