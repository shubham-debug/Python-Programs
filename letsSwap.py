# let's swap

def solve(arr):
    mx= max(arr)
    mi = min(arr)
    i1 = arr.index(mx)
    i2 = arr.index(mi)
    arr[i1],arr[i2]=arr[i2],arr[i1]
    ans = 0
    for i in range(len(arr)):
        ans += abs(arr[i]-1-i)
    return ans

if __name__=="__main__":
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(solve(arr))
