#program to find the square root of a number
#without using sqrt function

import math

def solve(n,i,j):
    mid=i+j
    mid=mid/2
    mul=mid*mid
    if(mul==n or abs(mul-n)<0.00001):
        return mid
    elif(mul<n):
        return solve(n,mid,j)
    else:
        return solve(n,i,mid)


#this is the naive brute force method
#it takes O(n*10**3) time to compute
def find(n):
    i=1
    while(i*i<n):
        i+=0.001
    return i



if __name__=="__main__":
    n=int(input("Enter the number\n"))
    print(math.sqrt(n))
    print(solve(n,0,n))
    print(find(n))
    
