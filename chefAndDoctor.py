#doctor chef
#this is not fully accepted
#i will learn it during the after contest discussion
#this is a copy

def solve(n,x,arr):
    arr.sort()
    if(arr[-1]<=x):
        return len(arr)
    count=0
    i=0
    while(x<arr[-1]):
        if(x>arr[i]):
            if(arr[i]*2>x):
                x=arr[i]*2
                count+=1
                arr[i]=0
            i+=1
        elif(x==arr[i]):
            arr[i]=0
            i+=1
            count+=1
            x+=x
        else:
            x+=x
            count+=1
    for i in arr:
        if(i!=0):
            count+=1
    return count
    


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n,x=map(int,input().split())
        arr=[int(i) for i in input().split()]
        print(solve(n,x,arr))
