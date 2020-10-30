#find the smallest binary digit multiple of given number

#simple bfs

def solve(n):
    l=[1]
    while(True):
        nt=list()
        while(len(l)):
            k=l.pop()
            if(k%n==0):
                return k
            else:
                nt.append(k*10)
                nt.append(k*10+1)
        l=nt[-1::-1]
        




if __name__=="__main__":
    n=int(input())
    print(solve(n))
