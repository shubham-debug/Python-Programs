#winning strategy

def solve(arr):
    p1=0
    p2=0
    arr.sort(reverse=True)
    p1=arr[0]
    if(len(arr)>=3):
        p2=arr[1]+arr[2]
    elif(len(arr)==2):
        p2=arr[1]
    count=3
    while(count<len(arr)):
        p1+=arr[count]
        count+=2
    count=4
    while(count<len(arr)):
        p2+=arr[count]
        count+=2
    if(p1>p2):
        return 'first'
    elif(p2>p1):
        return 'second'
    return 'draw'
        
        



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        print(solve(arr))
