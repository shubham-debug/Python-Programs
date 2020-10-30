#max sum in array such that no two elements are adjacent

def solve(arr):
    ans=0
    incl=arr[0]
    excl=0
    for i in arr[1:]:
        temp=incl
        incl=max(excl+i,incl)
        excl=temp
    return incl
    


if __name__=="__main__":
    l=[int(i) for i in input().split()]
    print(solve(l))
