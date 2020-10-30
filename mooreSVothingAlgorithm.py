#moore's voting algorithm
#find the majority element
#majority element is the element that occured more than n/2 times in an array
#time O(n) space O(1)

#brute force time O(n^2) space O(1)
def bruteForce(arr):
    majorityElement=-1
    for i in range(len(arr)):
        counter=0
        for j in range(len(arr)):
            if(arr[j]==arr[i]):
                counter+=1
        if(counter>len(arr)//2):
            majorityElement=arr[i]
            break
    return majorityElement


#use of hashmap time O(n) space O(n)
def hashmap(arr):
    count=dict()
    for i in arr:
        if(i in count):
            count[i]+=1
        else:
            count[i]=1
    ans=-1
    for i in count:
        if(count[i]>len(arr)//2):
            ans=i
    return ans


#pivot
def pivot(arr,l,r):
    p=arr[l]
    j=r
    for i in range(r,l,-1):
        if(arr[i]>=p):
            arr[j],arr[i]=arr[i],arr[j]
            j-=1
    #print(j)
    arr[l],arr[j]=arr[j],arr[l]
    return j
            


#use of sorting time O(nlgn) space O(1)
def quickSort(arr,l,r):
    if(l<r):
        p=pivot(arr,l,r)
        #print(p)
        quickSort(arr,l,p)
        quickSort(arr,p+1,r)
    return arr

#finding majority using sorting
def findMajority(arr):
    z=quickSort(arr[:],0,len(arr)-1)
    count=0
    current=z[0]
    for i in z:
        if(current==i):
            count+=1
            if(count>len(z)//2):
                return i
        else:
            current=i
            count=1
    return -1



#moore's voting algorithm
def moore(arr):
    expected=arr[0]
    count=1
    for i in range(1,len(arr)):
        if(arr[i]!=expected):
            count-=1
        else:
            count+=1
        if(count==0):
            expected=arr[i]
    count=0
    for i in range(len(arr)):
        if(arr[i]==expected):
            count+=1
    if(count>len(arr)//2):
        return expected
    return -1

#learn about how to code with bits of an integer
#to be done tomorrow
def bitmask():
    pass
    
        
    


if __name__=="__main__":
    arr=[int(i) for i in input("Enter the array\n").split()]
    print(bruteForce(arr))
    print(hashmap(arr))
    print(findMajority(arr))
    print(moore(arr))
    
    
    











    
