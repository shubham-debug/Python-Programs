#profits by cars


def solve(arr):
    k=set(arr)
    ans=0
    for i in k:
        ans+=i
    return ans
    





    



if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=[int(j) for j in input().split()]
        print(solve(arr))
