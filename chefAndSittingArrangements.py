    #chef and wedding arrangements

def solve(k,arr):
    s=set()
    ans=0
    for i in range(len(arr)):
        if(arr[i] not in s):
            s.add(arr[i])
        else:
            ans+=1
            s=set()
            s.add(arr[i])
    return ans+1

def ss(k,arr):
    temp=dict()
    for i in arr:
        if(i in temp):
            temp[i]+=1
        else:
            temp[i]=1
    ans=0
    for i in temp:
        if(temp[i]>1):
            ans+=temp[i]
    return ans+k

def nuta(k,arr):
    s=set()
    ans=1
    for i in arr:
        if(i not in s):
            s.add(i)
        else:
            s={i}
            ans+=1
    return k*ans
            



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        if(k==1):
            print(solve(k,arr))
        else:
            a1=ss(k,arr)
            a2=nuta(k,arr)
            print(min(a1,a2))
