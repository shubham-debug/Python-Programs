#finding the factors of a number
#time complexity of the code is O(sqrt(n))

def solve(n):
    ans=list()
    i=1
    while(i*i<=n):
        if(n%i==0):
            ans.append(i)
            if(n//i!=i):
                ans.append(n//i)
        i+=1

    return ans


def standard(n):
    ans=list()
    for i in range(1,n//2+1):
        if(n%i==0):
            ans.append(i)
    ans.append(n)
    return ans



if __name__=="__main__":
    n=int(input("Enter the number\n"))
    #print("solve using brute force")
    #print(*standard(n))
    #k=int(input())
    #print("solve using efficient algo")
    print(*solve(n))
