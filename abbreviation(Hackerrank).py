#conversion of string hackerank dynamic problem

def solve(a,b):
    counter=0
    j=0
    while(counter<len(a)):
        if(j>=len(b)):
            if(ord(a[counter])>=65 and ord(a[counter])<=90):
                j=-1
                break
            else:
                counter+=1
                continue
        if(a[counter]==b[j]):
            counter+=1
            j+=1
        elif(ord(a[counter])>=65 and ord(a[counter])<=90):
            if(j>=len(b)):
                j=-1
            break
        elif(ord(a[counter])-32==ord(b[j])):
            counter+=1
            j+=1
        else:
            counter+=1
    if(j>=len(b)):
        return "YES"
    return "NO"






    



if __name__=="__main__":
    t=int(input())
    for i in range(t):
        a=input()
        b=input()
        print(solve(a,b))
