#match making

def solve(boy,girl):
    boy.sort()
    boy=boy[-1::-1]
    girl.sort()
    ans=0
    for i in range(len(boy)):
        if(boy[i]%girl[i]==0 or girl[i]%boy[i]==0):
            ans+=1
    return ans


if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        girl=[int(i) for i in input().split()]
        boy=[int(i) for i in input().split()]
        print(solve(boy,girl))
