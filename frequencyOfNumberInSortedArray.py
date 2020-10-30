# this program is to find the frequency of number in a sorted array
# the time complexity of this program should be O(lg n)
# approach binary search

def solve(arr,start,end,key):
    if(arr[start] == arr[end-1] == key):
        return end-start
    if(start>end-1):
        return 0
    mid = start + end
    mid = mid//2
    if(arr[mid] == key):
        return 1 + solve(arr,start,mid,key) + solve(arr,mid+1,end,key)
    elif(arr[mid]>key):
        return solve(arr,start,mid,key)
    else:
        return solve(arr,mid+1,end,key)
    



if __name__=="__main__":
    arr = [int(i) for i in input().split()]
    n = int(input())
    print(solve(arr,0,len(arr),n))
