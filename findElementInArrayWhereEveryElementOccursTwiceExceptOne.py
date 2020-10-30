#find the element that occurs only once in an array where every element
#occurred twice

l=[int(i) for i in input("Enter the array\n").split()]
ans=l[0]
for i in l[1:]:
    ans=ans^i
print(ans)
