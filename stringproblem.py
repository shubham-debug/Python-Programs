#string problem
#this code is right for substring but not absolutely

def solve(n,s):
    j=0
    for i in range(1,n):
        if(s[i]>s[i-1]):
            j=i
            continue
    return(s[j:])



if __name__=="__main__":
    n=int(input())
    s=input()
    print(solve(n,s))
