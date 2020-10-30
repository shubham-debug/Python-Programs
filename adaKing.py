#ada king
#it is solved using simple dfs
#in the name of god the almighty

def solve(k):
    board=[[False for i in range(8)] for j in range(8)]
    x=0
    y=0
    board[x][y]=True
    util(board,x,y,k-1)
    pt(board)
    
    
def pt(board):
    flag=0
    for i in board:
        for j in i:
            if(j):
                if(flag==0):
                    print('O',end="")
                    flag=1
                else:
                    print('.',end="")
            else:
                print('X',end="")
        print()
    
def util(board,x,y,k):
    if(k>0):
        if(x+1<8 and y<8 and not board[x+1][y]):
            board[x+1][y]=True
            util(board,x+1,y,k-1)
            
        elif(x+1<8 and y-1>=0 and not board[x+1][y-1]):
            board[x+1][y-1]=True
            util(board,x+1,y-1,k-1)
            
        elif(x+1<8 and y+1<8 and not board[x+1][y+1]):
            board[x+1][y+1]=True
            util(board,x+1,y+1,k-1)
            
        elif(x<8 and y-1>=0 and not board[x][y-1]):
            board[x][y-1]=True
            util(board,x,y-1,k-1)
            
        elif(x<8 and y+1<8 and not board[x][y+1]):
            board[x][y+1]=True
            util(board,x,y+1,k-1)
            
        elif(x-1>=0 and y-1>=0 and not board[x-1][y-1]):
            board[x-1][y-1]=True
            util(board,x-1,y-1,k-1)
            
        elif(x-1>=0 and y<8 and not board[x-1][y]):
            board[x-1][y]=True
            util(board,x-1,y,k-1)
            
        elif(x-1>=0 and y+1<8 and not board[x-1][y+1]):
            board[x-1][y+1]=True
            util(board,x1,y+1,k-1)
        
            

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        k=int(input())
        if(k<64):
            solve(k)
        else:
            board=[[True for i in range(8)] for j in range(8)]
            pt(board)






        
