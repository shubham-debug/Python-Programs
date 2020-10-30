#priority scheduling algorithm
#it also need improvement by using heap


def update(process,wait,counter,q):
    if(counter<len(process)):
        if(wait<=process[counter][0]):
            flag=process[counter][0]
        else:
            flag=wait
        while(counter<len(process) and process[counter][0]<=flag):
            q.append(process[counter])
            counter+=1
        q=sorted(q,key = lambda x:x[2])
        return(q,counter)
    return(q,counter)


def solve(process):
    n=len(process)
    waiting=[0]*n
    #wait is actually the variable to store the current unit of time of computer
    #not actually the wait for each process but the unit time when of the
    #computer when certain process is finished and another one arrived
    #i know it is now a bit complicated but i undrestand it...
    wait=0
    counter=0
    q=list()
    while(counter<n):
        q,counter=update(process,wait,counter,q)
        while(q):
            z=q.pop(0)
            if(wait<=z[0]):
                waiting[z[3]]=0
                wait=z[0]+z[1]
            else:
                waiting[z[3]]=wait-z[0]
                wait+=z[1]
            q,counter=update(process,wait,counter,q)
    return(waiting)



#preemptive of priority scheduling
def updatee(process,n,counter,q,wait):
    if(counter<n):
        if(wait<=process[counter][0]):
            flag=process[counter][0]
        else:
            flag=wait
        while(counter<len(process) and process[counter][0]<=flag):
            q.append(process[counter])
            counter+=1
        q=sorted(q,key = lambda x:x[2])
        return(q,counter)

    return(q,counter)




def solvee(process,burst):
    n=len(process)
    waiting=[0]*n
    wait=0
    counter=0
    q=list()
    while(counter<n):
        q,counter=updatee(process,n,counter,q,wait)
        while(q):
            z=q.pop(0)
            a=z[0]
            b=z[1]
            if(counter<n and (a+b)<=process[counter][0]):
                if(wait<=z[0]):
                    waiting[z[3]]=0
                    wait=z[0]+z[1]
                else:
                    waiting[z[3]]=wait-z[0]
                    wait+=z[1]
                q,counter=updatee(process,n,counter,q,wait)
            elif(counter<n):
                wait+=process[counter][0]-z[0]
                z[1]-=process[counter][0]-z[0]
                q.append(z)
                q,counter=updatee(process,n,counter,q,wait)
            else:
                if(wait<=z[0]):
                    waiting[z[3]]=0
                    wait=z[0]+z[1]
                else:
                    wait+=z[1]
                    tat=wait-z[0]
                    waiting[z[3]]=tat-burst[z[3]]
    return(waiting)
                
                
                
                
            

if __name__=="__main__":
    arrival=[int(i) for i in input().split()]
    burst=[int(i) for i in input().split()]
    priority=[int(i) for i in input().split()]
    process=list()
    for i in range(len(arrival)):
        process.append([arrival[i],burst[i],priority[i],i])
    #process = sorted(process, key=lambda x:x[2])
    process = sorted(process)
    print(*solvee(process,burst))
