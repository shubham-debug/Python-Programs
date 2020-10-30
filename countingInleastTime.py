from collections import Counter

def cout(l):
    d=dict()
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


def coutt(l):
    d=Counter(l)
    return dict(d)
    
if __name__=="__main__":
    l=[1,1,2,4,3,4,1,2,3,2,4]
    d=coutt(l)
    print(d)
    for i in d:
        print(i)
