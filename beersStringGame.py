# number of string


def solve(fav,t):
    s=set(fav)
    ans=0
    for i in t:
        if(set(i).issubset(s)):
            ans+=1
    return ans
            












if __name__=="__main__":
    fav=input()
    t=int(input())
    l=list()
    for i in range(t):
        l.append(input())

    print(solve(fav,t))
