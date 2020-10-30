#a product array puzzle

def solve(arr):
    if(len(arr)==1):
        return 0
    ans=[1 for i in range(len(arr))]
    temp=1
    for i in range(len(arr)):
        ans[i]=temp
        temp*=arr[i]
    temp=1
    for i in range(len(arr)-1,-1,-1):
        ans[i]*=temp
        temp*=arr[i]
    return ans
        
        

if __name__=="__main__":
    arr=[int(i) for i in input().split()]
    print(solve(arr))
