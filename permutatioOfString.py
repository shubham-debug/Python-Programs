#permutation of a string

def solve(s,l,r):
    if(l==r):
        print(s)
    else:
        for j in range(l,r+1):
            s[j],s[l]=s[l],s[j]
            solve(s,l+1,r)
            s[j],s[l]=s[l],s[j]
    



if __name__=="__main__":
    s=input()
    real=list(s)
    solve(real,0,len(s))
