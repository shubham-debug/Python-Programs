# A problem on sticks

def solve(arr):
    temp=set(arr)
    k=len(temp)
    if(0 in temp):
        k-=1
    #print(temp)
    return k
    



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        print(solve(arr))
