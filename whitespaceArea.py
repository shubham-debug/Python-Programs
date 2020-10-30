#area of white space
#problem hackerearth: Roy and Diamonds
#this solution is fully accepted
#In the name of god the almighty one

def solve(h,w):
    area=h*w
    nd=w//2
    if(w%2==0):
        nd1=nd-1
    else:
        nd1=nd
    num=0
    k=h//4
    if(h-(k*4)>=2):
        k1=k
    else:
        k1=k-1
        
    num+=k*nd
    num+=k1*nd1
    area1=num*2*2
    return area-area1
       

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        h,w=map(int,input().split())
        print(solve(h,w))
