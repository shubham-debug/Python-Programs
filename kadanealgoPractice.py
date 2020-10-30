#kadane algorithm

def kadane(arr):
    ans=float('-inf')
    temp=float('-inf')
    for i in arr:
        temp=max(temp+i,i)
        ans=max(temp,ans)
    return ans



if __name__=="__main__":
    l=[int(i) for i in input().split()]
    print(kadane(l))
