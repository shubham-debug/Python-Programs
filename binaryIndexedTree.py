#binary indexed tree
#alternative segment tree


def getSum(bit,i):
    s=0
    i=i+1
    while(i>0):
        s+=bit[i]
        i-=i&(-i)
    return s



def updateSum(bit,i,val):
    i+=1
    while(i<=len(bit)-1):
        bit[i]+=val
        i+=i & (-i)


def construct(bit,arr):
    for i in range(len(arr)):
        updateSum(bit,i,arr[i])




if __name__=="__main__":
    arr=[int(i) for i in input().split()]
    bit=[0 for i in range(len(arr)+1)]
    construct(bit,arr)
    print(bit)
    q=int(input("Enter the number of queries\n"))
    for i in range(q):
        flag=int(input("Enter 0 for update and 1 for sum\n"))
        if(flag):
            n=int(input("Enter the range\n"))
            print(getSum(bit,n))
        else:
            n,a=map(int,input("Enter the values\n").split())
            arr[n-1]=a
            updateSum(bit,n,a)
