#smallest kmp
#accepted

def solve(s,p):
    ans=''
    temp=dict()
    for i in s:
        if(i in temp):
            temp[i]+=1
        else:
            temp[i]=1
    temp1=dict()
    for i in p:
        if(i in temp1):
            temp1[i]+=1
        else:
            temp1[i]=1
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'
       ,'s','t','u','v','w','x','y','z']
    for i in l:
        if(i in temp):
            ans+=i*temp[i]
    #print(ans)
    ans=''
    ans1=''
    for i in l:
        if(i==p[0]):
            z=i*(temp[i]-temp1[i])
            ans+=z
            ans+=p
            ans1+=p
            ans1+=z
        else:
            if(i in temp):
                if(i not in temp1):
                    z=i*temp[i]
                else:
                    z=i*(temp[i]-temp1[i])
                ans+=z
                ans1+=z
    #print(len(ans))
    return min(ans,ans1)

if __name__=="__main__":
    t=int(input())
    for test in range(t):
        s=input()
        p=input()
        #print(len(s))
        print(solve(s,p))
