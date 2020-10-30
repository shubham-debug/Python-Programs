#chef wars - return of the jedi

def solve(h,p):
    while(h>0 and p>0):
        h-=p
        p//=2
    if(h<=0):
        return 1
    return 0




    



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        h,p=map(int,input().split())
        print(solve(h,p))
