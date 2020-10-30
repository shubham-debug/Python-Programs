#max number of vowel in any substring of length k
#example : s= "abciiidef",k=3
#output should be 3
#dynamic programming
#time complexity O(n)

if __name__=="__main__":
    s=input()
    k=int(input())
    test={'a','e','i','o','u'}
    temp=[0 for i in range(len(s))]
    mx=-1
    counter=0
    for i in range(len(s)):
        if(s[i] in test):
            counter+=1
        temp[i]=counter
    for i in range(k-1,len(s)):
        mx=max(mx,temp[i]-temp[i-k])
    print(mx)
        
    

    
