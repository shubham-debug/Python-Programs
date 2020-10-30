# N Queen Problem (backtracking algorithm)
# I don't know how to solve this problem so this will take some time
# as I donot prefer to see the solution before even approaching the problem
# although I have hint that this is solved using backtracking
# Input : N denoting the number of queens although the expected number is 4/8
# Output: a N*N matrix showing the position of the queen in the chess board
#         If no position is possible output is -1

def generateBoard(n):
    board=[[0 for i in range(n)] for j in range(n)]
    return board

def isSafe(board,i,j,n):
    for z in range(n):
        if(z==i):
            continue
        if(board[z][j]==1):
            return False
    d1=i-1
    d2=j-1
    while(d1>=0 and d2>=0):
        if(board[d1][d2]==1):
            return False
        d1-=1
        d2-=1
    d1=i-1
    d2=j+1
    while(d1>=0 and d2<n):
        if(board[d1][d2]==1):
            return False
        d1-=1
        d2+=1
    return True


def solve(board,i,n):
    if(i==n):
        return True
    for j in range(n):
        if(isSafe(board,i,j,n)):
            board[i][j]=1
            if(solve(board,i+1,n)):
                return True
            board[i][j]=0
    return False
        
                

if __name__=="__main__":
    n=int(input())
    board=generateBoard(n)
    #print(board)
    if(solve(board,0,n)):
        for i in board:
            print(*i)
    else:
        print('solution does not exists')
