#function for binary representation of a number

def binary(n):
    s=str()
    while(n>0):
        z=n%2
        s+=str(z)
        n//=2
    return s


n=int(input("Enter the number\n"))
print(binary(n))
print(bin(n)[2:])
