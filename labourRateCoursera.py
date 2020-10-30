


def solve(hours, rate):
    if(hours<=40):
        return hours*rate
    return (40*rate)+((hours-40)*(rate*1.5))

if __name__=="__main__":
    hours = int(input("Enter the hours\n"))
    rate = float(input("Enter the rate\n"))
    print(solve(hours, rate))
    
    
