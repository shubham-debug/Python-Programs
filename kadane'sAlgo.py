#kadane's algorithm
#finding the maximum sum of subarray present in the given array


#the input array
arr=[int(i) for i in input("Enter the elements of array\n").split()]
#variable to keep track of the maxsum subarray upto a given position in array
#initialized with array first element
maxGlobal=arr[0]
maxCurrent=arr[0]
for i in range(1,len(arr)):
    #variable to store the maxcurrent
    maxCurrent=max(arr[i],maxCurrent+arr[i])
    if(maxCurrent>maxGlobal):
        maxGlobal=maxCurrent

print(maxGlobal)
