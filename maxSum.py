#maximum sum such that no two elements are adjacent

arr=[int(i) for i in input().split()]
incl=0
excl=0
for i in arr:
    temp=incl
    incl=max(incl,excl+i)
    excl=temp

print(incl)
