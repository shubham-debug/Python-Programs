#chef and linear chess

def solve(k,arr):
    mi=float('inf')
    z=-1
    for i in arr:
        if(k%i==0):
            temp=k//i
            if(temp<mi):
                mi=temp
                z=i
    if(mi==float('inf')):
        return -1
    return z
    


if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        print(solve(k,arr))
