#chef and card game

if __name__=="__main__":
    t=int(input())
    for j in range(t):
        chef=0
        morty=0
        n=int(input())
        for i in range(n):
            a,b=input().split()
            a1=0
            b1=0
            for k in a:
                a1+=int(k)
            for k in b:
                b1+=int(k)
            if(a1>b1):
                chef+=1
            elif(a1<b1):
                morty+=1
            else:
                chef+=1
                morty+=1
        if(chef>morty):
            print('0',chef)
        elif(morty>chef):
            print('1',morty)
        else:
            print('2',chef)
            
