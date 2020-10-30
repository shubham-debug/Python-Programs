#smalles kmp

def solve(s,p):
    ans=''
    d=dict()
    for i in s:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1

    l=list()
    for i in range(ord('a'),ord('z')+1):
        l.append(chr(i))
    temp=dict()
    for i in p:
        if(i in temp):
            temp[i]+=1
        else:
            temp[i]=1
    for i in l:
        if(i==p[0]):
            z=i*(d[i]-temp[i])
            ans+=z
            ans+=p
        
        



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        s=input()
        p=input()
        print(solve(s,p))
