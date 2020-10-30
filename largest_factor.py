#largest common factor
import math
def lcd(i):
    n=1
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            n=i//j
            break
    return n

print(lcd(9999999967))
