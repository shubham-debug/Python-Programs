# the ugly number

#this function divides a by the greates divisible power of b
def maxDivide(a,b):
    while(a%b==0):
        a = a//b
    return a


# function to check if a number id ugly or not
def isUgly(num):
    num = maxDivide(num,2)
    num = maxDivide(num,3)
    num = maxDivide(num,5)
    return num == 1



# brute force method to solve ugly number
def bruteForce(n):
    count = 1
    i = 1
    while(count<n):
        i += 1
        if(isUgly(i)):
            count += 1
    return i 


    
if __name__=="__main__":
    n = int(input("Enter the position\n"))
    num = bruteForce(n)
    print(num)
