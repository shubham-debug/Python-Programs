#bobble sort a june circuits

def solve(a):
    count=0
    n=len(a)
    swapped = True
    while(swapped):
        swapped=False
        count+=1
        for i in range(1,n-1):
            if(a[i]>a[i+1]):
                a[i],a[i+1]=a[i],a[i+1]
                swapped=True
    return count


def solvee(a):
    mn=a[0]
    counter=0
    for i in range(1,len(a)):
        if(a[i]<mn):
            counter+=1
        mn=min(a[i],mn)
    return counter


if __name__=="__main__":
    n=int(input())
    a=[int(i) for i in input().split()]
    print(solvee(a))
