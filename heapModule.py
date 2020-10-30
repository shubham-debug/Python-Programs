# how to use heap module in python
import heapq

class minheap:

    def __init__(self,l):
        self.heap=l
        heapq.heapify(self.heap)


    def __str__(self):
        return str(self.heap)

    def pushitem(self,key):
        heapq.heappush(self.heap,key)

    def extractmin(self):
        return self.heap[0]

    def popitem(self):
        return heapq.heappop(self.heap)

    def pushpopitem(self,key):
        return heapq.heappushpop(self.heap,key)

    def replaceitem(self,key):
        return heapq.heapreplace(self.heap,key)

    def mergeheap(self,list1):
        #it works for the iterable that are already sorted
        self.heap=list(heapq.merge(self.heap,list1))

    def nlargest(self,n):
        return heapq.nlargest(n,self.heap)

    def nsmallest(self,n):
        return heapq.nsmallest(n,self.heap)




if __name__=="__main__":
    k=minheap([3,5,2,7,90])
    print("here is the initail heap\n",k)
    k.pushitem(57)
    print("here is the heap after pushing the item\n",k)
    print(k.popitem())
    print("here is the heap after pop\n",k)
    print("here is the minimum element of the list\n",k.extractmin())
    k.pushpopitem(156)
    print("here is the heap after pushpop\n",k)
    k.replaceitem(2045)
    print("here is the heap after reaplace\n",k)
    k.mergeheap([-45,0,4,7,9,19])
    print("here is the heap after merging\n",k)
    print(k.nlargest(4))
    print(k.nsmallest(5))






    
        
