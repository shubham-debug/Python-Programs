#operation on an array
#hacker earth
#this is not accepted

def find(arr,temp,x):
    l,r,k=temp
    counter=0
    for i in range(l-1,r):
        if(arr[i]==x):
            counter+=1
        if(counter==k):
            return i+1
    return -1

n,x=map(int,input().split())
arr=[int(i) for i in input().split()]
if(len(arr)!=n):
    for i in range(1,n):
        arr.append(int(input()))
q=int(input())
for i in range(q):
    temp=[int(j) for j in input().split()]
    if(len(temp)==4):
        print(find(arr,temp[1:],x))
    else:
        arr[temp[1]-1]=temp[2]
        
