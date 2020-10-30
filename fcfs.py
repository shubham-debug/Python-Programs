#all scheduling algorithms
#i am gonna improve all the algorithms aftere learning segment tree and
#revising heap again

def fcfs(arrival,burst):
    waiting=list()
    wait=0
    for i in range(len(arrival)):
        if(wait<=arrival[i]):
            wait=0
            waiting.append(wait)
            wait=arrival[i]+burst[i]
            continue
        waiting.append(wait-arrival[i])
        wait+=burst[i]
    return(waiting)




#shortes job first(non-preemptive)
#it is needed to be improved by using heap and segment tree
def update_queue(q,arrival,a,burst,wait,counter,n):
    if(counter<n):
        
        if(wait<=arrival[counter]):
            flag=arrival[counter]
        else:
            flag=wait
        while(arrival[counter]<=flag and counter<n):
            i=a[arrival[counter]].pop(0)
            q.append(burst[i])
           
            counter+=1
            if(counter>=n):
                break
        q.sort()
        return(q,counter)
        
    return(q,counter)
        
        






def sjff(arrival,burst):
    n=len(arrival)
    waiting=[0]*n

    #waiting queue
    q=list()
    #dictionary to store the index of arrival time
    #with respect to the current index before sorting
    a=dict()
    b=dict()
    for i in range(n):
        if(burst[i] in b):
            b[burst[i]].append([arrival[i],i])
        else:
            b[burst[i]]=[[arrival[i],i]]
        if(arrival[i] in a):
            a[arrival[i]].append(i)
        else:
            a[arrival[i]]=[i]
    #initialize wait variable to store wait
    wait=0
    counter=0
    arrival.sort()
    while(counter<n):
        q,counter=update_queue(q,arrival,a,burst,wait,counter,n)
        while(q):
            z=q.pop(0)
            i=b[z][0][1]
            t=b[z][0][0]
            b[z].pop(0)
            if(wait<=t):
                waiting[i]=0
                wait=t+z
            else:
                waiting[i]=wait-t
                wait+=z
            q,counter=update_queue(q,arrival,a,burst,wait,counter,n)
  

    return(waiting)
        
            
        


if __name__=="__main__":
    arrival=[int(i) for i in input("Enter the arrival time\n").split()]
    burst=[int(i) for i in input("Enter the burst time\n").split()]
    print('The waiting time of the process:')
    #print(*fcfs(arrival,burst))
    print(*sjff(arrival,burst))
    
