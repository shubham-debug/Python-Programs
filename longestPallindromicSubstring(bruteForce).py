#longest pallindromic substring brute force method
#it does not satisfy all the test cases

def find(s):
    mx=0
    idx=0
    for i in range(len(s)):
        a=i
        b=i
        counter=1
        while(True):
            if(a>0 and b<(len(s)-1)):
                a-=1
                b+=1
                if(s[a]==s[b]):
                    counter+=1
                    continue
            break
        if(counter>mx):
            mx=counter
            idx=i
    k=""
    for i in range(idx-mx+1,idx+mx):
        k+=s[i]
    return k



if __name__=="__main__":
    s=input("Enter the string\n")
    print("Longest pallindromic substring is:")
    print(find(s))
