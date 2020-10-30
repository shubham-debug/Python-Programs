#tic tac toe game
import random

from os import system, name

from time import sleep

def startGame(board):
    while(True):
        player=input('Chose your mark(X or 0)\n')
        if(player!= '0' and player!='X'):
            continue
        break
    if(player=='0'):
        comp='X'
    else:
        comp='0'
    #makeTurn(board,player)
    #printBoard(board,player,comp)

    move=random.choice([0,1])
    #move=1
    while(True):
        if(move):
            makeTurn(board,player)
            move=0
        else:
            compTurn(board,comp)
            move=1
        z=checkWinner(board)
        system('cls')
        printBoard(board,player,comp)
        if(z):
            if(z=='Draw'):
                print('Draw')
            elif(z==player):
                print('Winner player')
            else:
                print('Winner comp')
            break
            
        
        
        
def compTurn(board,comp):
    count=0
    for i in board:
        if(board[i]!=''):
            count+=1

    if(count==0):
        board['tl']=comp
        
    elif(count==1):
        if(board['tl']!='' and board['tr']!='' and board['bl']!='' and board['br']!=''):
            board['tl']=comp
        else:
            board['mm']=comp
    elif(count==2):
        if(board['tr']==''):
            board['tr']=comp
        elif(board['br']==''):
            board['br']=comp
        else:
            board['bl']=comp


    elif(board['tl']==board['tm']!='' and board['tr']==''):
        board['tr']=comp
        
    elif(board['tl']==board['tr']!='' and board['tm']==''):
        board['tm']=comp
        
    elif(board['tm']==board['tr']!='' and board['tl']==''):
        board['tl']=comp
        
    elif(board['ml']==board['mm']!='' and board['mr']==''):
        board['mr']=comp
        
    elif(board['ml']==board['mr']!='' and board['mm']==''):
        board['mm']=comp
        
    elif(board['mm']==board['mr']!='' and board['ml']==''):
        board['ml']=comp
        
    elif(board['bl']==board['bm']!='' and board['br']==''):
        board['br']=comp
        
    elif(board['bl']==board['br']!='' and board['bm']==''):
        board['bm']=comp
        
    elif(board['bm']==board['br']!='' and board['bl']==''):
        board['bl']=comp

    elif(board['tl']==board['bl']!='' and board['ml']==''):
        board['ml']=comp

    elif(board['ml']==board['bl']!='' and board['tl']==''):
        board['tl']=comp

    elif(board['tl']==board['ml']!='' and board['bl']==''):
        board['bl']=comp

    elif(board['tm']==board['bm']!='' and board['mm']==''):
        board['mm']=comp

    elif(board['mm']==board['bm']!='' and board['tm']==''):
        board['tm']=comp

    elif(board['tm']==board['mm']!='' and board['bm']==''):
        board['bm']=comp

    elif(board['tr']==board['br']!='' and board['mr']==''):
        board['mr']=comp

    elif(board['mr']==board['br']!='' and board['tr']==''):
        board['tr']=comp

    elif(board['tr']==board['mr']!='' and board['br']==''):
        board['br']=comp

    elif(board['tl']==board['br']!='' and board['mm']==''):
        board['mm']=comp

    elif(board['tr']==board['bl']!='' and board['mm']==''):
        board['mm']=comp

    count1=0
    for i in board:
        if(board[i]!=''):
            count1+=1
    if(count1==count):
        if(board['tl']==''):
            board['tl']=comp
        elif(board['tr']==''):
            board['tr']=comp
        elif(board['bl']==''):
            board['bl']=comp
        elif(board['br']==''):
            board['br']=comp
        else:
            for i in board:
                if(board[i]==''):
                    board[i]=comp
                    break
        
    


def makeTurn(board,player):
    s=set()
    for i in board:
        if(board[i] == ''):
            s.add(i)
            print(i,end=' ')
    print('Enter one of the following to fill')
    while(True):
        k=input()
        if(k in s):
            board[k]=player
            break
        else:
            print('please enter a valid option')
    


    


#this will return which move win
def checkWinner(board):
    if((board['tl']==board['tm']==board['tr']=='X') or
       (board['ml']==board['mm']==board['mr']=='X') or
       (board['bl']==board['bm']==board['br']=='X') or
       (board['tl']==board['mm']==board['br']=='X') or
       (board['bl']==board['mm']==board['tr']=='X') or
       (board['tl']==board['ml']==board['bl']=='X') or
       (board['tm']==board['mm']==board['bm']=='X') or
       (board['tr']==board['mr']==board['br']=='X')):
        return 'X'
    elif((board['tl']==board['tm']==board['tr']=='0') or
       (board['ml']==board['mm']==board['mr']=='0') or
       (board['bl']==board['bm']==board['br']=='0') or
       (board['tl']==board['mm']==board['br']=='0') or
       (board['bl']==board['mm']==board['tr']=='0') or
       (board['tl']==board['ml']==board['bl']=='0') or
       (board['tm']==board['mm']==board['bm']=='0') or
       (board['tr']==board['mr']==board['br']=='0')):
        return '0'
    for i in board:
        if(board[i]==''):
            return False
    return 'Draw'





def printBoard(board,player,comp):
    print('\n\nplayer move: {0}   computer move: {1}\n\n'.format(player,comp))
    count=0
    flag=0
    for i in board:
        print(board[i],end=' ')
        count+=1
        if(count>=3):
            flag+=1
            count=0
            print()
            if(flag<3):
                print('-------------')
        else:
            print(' | ',end=' ')
        




if __name__=="__main__":
    system('cls')
    board={

            'tl':'', 'tm':'', 'tr':'',
            'ml':'', 'mm':'', 'mr':'',
            'bl':'', 'bm':'', 'br':''

        }
    #printBoard(board)
    startGame(board)
    
        










        
