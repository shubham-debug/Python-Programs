# corona virus spread codechef septermber challenge

def solve(n,arr):
    best=0
    worst=0
    z=arr[:]
    z.sort()
    



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        print(solve(n,arr))
