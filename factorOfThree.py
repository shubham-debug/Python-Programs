#factor of 3

def solve(arr):
    d=dict()
    d[0]=0
    d[1]=0
    d[2]=0
    for i in arr:
        if(i%3==0):
            d[0]+=1
        elif(i%3==1):
            d[1]+=1
        else:
            d[2]+=1
    if((d[0]==0 and d[1]!=0 and d[2]!=0) or (d[0]>d[1]+d[2]+1)):
        return 'No'
    return 'Yes'

            
    
    



if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        print(solve(arr))
