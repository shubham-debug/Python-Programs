# and choice
# this is accepted
# and from this question i learn about bitmasking

# this could be solved using bitmasking
def solve(arr):
    mask = 0
    for i in range(31,-1,-1):
        count = 0
        for j in range(len(arr)):
            if((arr[j]&(mask|1<<i)) == (mask|1<<i)):
                count+=1
        if(count>=2):
            mask |= 1<<i
    return mask
                



if __name__=="__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(solve(arr))
