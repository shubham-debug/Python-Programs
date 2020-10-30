#print all permutation of a string

def change(s):
    return ''.join(s)

def solve(s,l,r):
    if(l==r):
        print(change(s))
    else:
        for i in range(l,r+1):
            s[i],s[l]=s[l],s[i]
            solve(s,l+1,r)
            s[i],s[l]=s[l],s[i]

        


s=input()
solve(list(s),0,len(s)-1)
