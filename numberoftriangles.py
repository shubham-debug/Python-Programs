#number of triangles

def solve(n):
    ans=(n*2)+(n*6)+(6*(n-1))
    return ans

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        print(solve(int(input())))
