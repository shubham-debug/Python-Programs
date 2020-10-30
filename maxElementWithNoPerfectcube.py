#you are given a sequence of non-negative numbers and you are required to put
#some of these numbers into a bucket such that :
#The product of any two distinct elements in the bucket is not a cube and the
#numbers in the bucket must be maximum

#Now, your task is to determine the maximum number of elements in the bucket.

#Input format

#The first line contains a single integer n.
#Each of the next  n lines contains elements of the sequence
#Output format

#Print the maximum number of elements in the bucket

def isperfect(a):
    b=a**(1/3)
    if(b**3==int(b)**3):
        return True
    return False


def isPrime(n) : 
  
    # Corner cases 
    if (n < 1) : 
        return False
    if(n==1):
        return True
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True




if __name__=="__main__":
    n=int(input())
    ans=0
    l=list()
    bucket=list()
    k1=list()
    for i in range(n):
        l.append(int(input()))
        
    for i in range(n):
        if(isPrime(i)):
            bucket.append(i)
            ans+=1
        else:
            k1.append(i)

    for i in k1:
        for j in bucket:
            if(isperfect(i*j)):
                break
        else:
            bucket.append(i)
            ans+=1
            
    print(len(bucket))
            



        
        
