#Finding vaccines Hackerearth(august easy)

def solve(ans,g,c,vac):
    temp=0
    countg=0
    countc=0
    for i in vac:
        if(i=='G'):
            countg+=1
        if(i=='C'):
            countc+=1
    temp+=g*countc
    temp+=c*countg
    return temp
    


if __name__=="__main__":
    n=int(input())
    m=int(input())
    virus=input()
    countg=0
    countc=0
    for i in virus:
        if(i=='G'):
            countg+=1
        if(i=='C'):
            countc+=1
    ans=-1
    real=-1
    for i in range(n):
        l=int(input())
        vaccine=input()
        k=solve(ans,countg,countc,vaccine)
        if(k>ans):
            ans=k
            real=i+1
            
    print(real)
