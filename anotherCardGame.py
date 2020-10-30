#another card game problem
#accepted

def solve(n):
    sm=0
    temp=''
    n1=n
    '''while(sm<n):
        #print(sm)
        for i in range(9,0,-1):
            if(sm+i<=n):
                temp+=str(i)
                sm+=i
                break'''
    for i in range(9,0,-1):
        z=n1//i
        #print(z)
        if(sm+z*i<=n):
            sm+=z*i
            #print(sm)
            #print(n)
            n1-=z*i
            temp+=str(i)*z
    return temp
                


if __name__=="__main__":
    t=int(input())
    for test in range(t):
        c,r=map(int,input().split())
        cx=solve(c)
        rx=solve(r)
        #print(cx)
        #print(rx)
        if(len(rx)<=len(cx)):
            print(1,len(rx))
        else:
            print(0,len(cx))
