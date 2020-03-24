from IPython.display import clear_output



#prints out board 
def display_board(board):
    if len(board)==9:
        print('\n')
        print(board[0] + '|' +board[1] + '|' +board[2])
        print('- '+'- '+'- ')
        print(board[3] + '|' +board[4] + '|' +board[5])
        print('- '+'- '+'- ')
        print(board[6] + '|' +board[7] + '|' +board[8])
    elif len(board)==16:
        print(board[0] + '|' +board[1] + '|' +board[2] + '|' +board[3])
        print('- '+'- '+'- '+'- ')
        print(board[4] + '|' +board[5] + '|' +board[6] + '|' +board[7])
        print('- '+'- '+'- '+'- ')
        print(board[8] + '|' +board[9] + '|' +board[10] + '|' +board[11])
        print('- '+'- '+'- '+'- ')
        print(board[12] + '|' +board[13] + '|' +board[14] + '|' +board[15])


#player 1 select to X or O. P2 is given the other 
def player_assign():
    player_1 = ''
    player_2 = ''
    
    #initial state. Until p1 choses X or O it will not continue 
    while player_1 != 'X' and player_1!='O':
        player_1= input('Player 1, choose X or O: ')
        
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X' 
    
    print('Player 1 is :{}, and Player 2 is :{}.'.format(player_1,player_2))
    
    return (player_1,player_2)


def win_check(board):
    if board[0]==board[1]==board[2]!=' ' or board[3]==board[4]==board[5]!=' ' or board[6]==board[7]==board[8]!=' ':
        return True
    elif board[0]==board[4]==board[8]!=' ' or board[2]==board[4]==board[6]!=' ':
        return True
    elif board[0]==board[3]==board[6]!=' ' or board[1]==board[4]==board[7]!=' ' or board[2]==board[5]==board[8]!=' ':
        return True
    else:
        return False

def game_restart():
    game_select=''
    
    while game_select!='No' and game_select!='Yes':
        game_select = input('Would you like to start again???: ')
        
    if game_select=='yes' or game_select=='Yes':
        game_input()
    else:
        pass

def p1_turn(board,p1_mark):
    while True:
        position = int(input("Player 1's turn: "))
        if position==1234:
            game_restart()
        elif board[position-10]==' ':
            board[position-10]=p1_mark
            break
        else:
            pass

def p2_turn(board,p2_mark):
    while True:
        position = int(input("Player 2's turn: "))
        if postion==1234:
            game_restart()
        elif board[position-10]==' ':
            board[position-10]=p2_mark
            break
        else:
            pass

#game starts when called. Calls functions for setup and turn base algorrithm 
def game_input():  

    #calls for the funtion and stores the assgined marker for p1's and p2's slection.
    p1_mark,p2_mark = player_assign()
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    check_condition=False     

    #loops between 1 and 2 to start until wining conditions are met. Winning conditions are...
    #determined in the function win_check(board)
    while True:

        display_board(board)
        #player 1 starts
        p1_turn(board,p1_mark)
        check_condition = win_check(board)
        if check_condition==True:
            display_board(board)
            print('Player 1 wins!!')
            break
        else:
            pass

        display_board(board)
        #player 2 starts
        p2_turn(board,p2_mark)
        check_condition = win_check(board)
        if check_condition==True:
            display_board(board)
            print('Player 2 wins!!')
            break
        else:
            pass
    #option to restart the game   
    game_restart()
    
#initialize code
game_input()
   