#generating all subsequence of a list


def solve(arr,index,subarr,gen):
    if(index==len(arr)):
        if(len(subarr)!=0):
            gen.append(subarr)
    else:
        solve(arr,index+1,subarr,gen)
        solve(arr,index+1,subarr+[arr[index]],gen)

if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=[int(i) for i in input().split()]
        gen=list()
        solve(arr,0,[],gen)
        ans=dict()
        s=set()
        #print(gen)
        for i in arr:
            if(i not in ans):
                ans[i]=0
        for i in gen:
            temp=dict()
            for j in i:
                if(j in temp):
                    temp[j]+=1
                else:
                    temp[j]=1
            m=[float('inf'),float('-inf')]
            for i in temp:
                if(temp[i]>=m[1] and i<m[0]):
                    m=[i,temp[i]]
                elif(temp[i]>m[1]):
                    m=[i,temp[i]]
            #print(temp)
            #print(m)
            ans[m[0]]+=1
            #print(ans)
                
        real=list()
        for i in arr:
            if(i not in s):
                s.add(i%((10**9)+5)
                real.append(ans[i])
            else:
                real.append(0)
        print(*real)

















                
