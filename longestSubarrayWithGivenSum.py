# longest subarray with given sum


def solve(arr,sm):
    d={0:-1}
    tempsm=0
    l=-1
    r=-1
    mx=0
    for i in range(len(arr)):
        tempsm+=arr[i]
        z=tempsm-sm
        if(z in d):
            if(mx<(i-d[z])):
               l=d[z]+1
               r=i
               mx=i-d[z]
        d[tempsm]=i
    print(arr[l:r+1])
    


    




if __name__=="__main__":
    arr=[int(i) for i in input("Enter the array\n").split()]
    sm=int(input("Enter the sum\n"))
    print("The longest array with the given sum is:")
    solve(arr,sm)
