def find(arr,key):
    l=0
    r=0
    su=arr[0]
    while(l<len(arr)-1 and r<len(arr)):
        if(su==key and r<=l):
            for i in range(l,r+1):
                print(i,end=" ")
            return
        elif(su>key):
            su-=arr[r]
            r+=1
        else:
            l+=1
            su+=arr[l]
    print("No subarray is found")
    return
        
        


    



if __name__=="__main__":
    arr=input("Enter the array\n")
    ar=[int(i) for i in arr.split()]
    key=int(input("Enter the key\n"))
    find(ar,key)
