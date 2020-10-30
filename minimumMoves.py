#minimum moves

def solve(x,y):
    if(x<0 or y<0):
        return -1
    if(y>x):
        return -1
    return x

        


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        x,y=map(int,input().split())
        print(solve(x,y))
