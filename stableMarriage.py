# Gale-Shapely algorithm for stable matching problem





def solve(men,women):
    engWomen=dict()
    for i in range(



if __name__=="__main__":
    men = list()
    women = list()
    n=int(input("Enter the number of person in each set\n"))
    for i in range(n):
        temp=[int(j) for j in input("Enter the preference of men {}\n".format(i+1)).split()]
        men.append(temp)
    for i in range(n):
        temp=[int(j) for j in input("Enter the preference of women {}\n".format(i+1)).split()]
        women.append(temp)
    print(solve(men,women))
