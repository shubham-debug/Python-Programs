# ugly numbers dp

    
def solve(n):
    ugly = [0 for i in range(n)]
    ugly[0] = 1
    i2 = i3 = i5 = 0
    n2 = 2
    n3 = 3
    n5 = 5
    for i in range(1,n):
        ugly[i] = min(n2,n3,n5)
        if(ugly[i] == n2):
            i2 += 1
            n2 = ugly[i2]*2
        if(ugly[i] == n3):
            i3 += 1
            n3 = ugly[i3]*3
        if(ugly[i] == n5):
            i5 += 1
            n5 = ugly[i5]*5
            
    return ugly[-1]
    



if __name__=="__main__":
    n = int(input())
    print(solve(n))
    
