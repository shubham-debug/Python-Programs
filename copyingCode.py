#copying code
# hacker earth october easy

def solve(n,i):
    return min((4+n-i),2*(n-i))




if __name__=="__main__":
    n,i = map(int,input().split())
    print(solve(n,i))
