from IPython.display import clear_output

board_3x3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
board_4x4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def size_board(board_3x3):
    if len(board)==9:
        return 3
    elif len(board)==16:
        return 4
    else:
        print('Board size is unslected or unviable')
    

#prints out board 
def display_board(board_3x3):
        print(board[0] + '|' +board[1] + '|' +board[2])
        print('- '+'- '+'- ')
        print(board[3] + '|' +board[4] + '|' +board[5])
        print('- '+'- '+'- ')
        print(board[6] + '|' +board[7] + '|' +board[8])


def display_board(board_4x4):
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

#calls for the funtion and stores the assgined marker for p1's and p2's slection.
p1_mark,p2_mark = player_assign()

def check_condition():
    for char in range(len(board)):
        if board[char] == board[char+1] == board[char+2]: 
            print("WIN")
            return True
        else:
            return False



#game starst when called. Calls functions for setup and turn base algorrithm 
def game_input():       
    
    while check_condition!=True:
        clear_output()
        display_board(board)
        #player 1 starts
        position = int(input("Player 1's turn: "))
        board[position-10] = p1_mark
        
        check_condition()

        clear_output()
        
        #player 2 starts
        display_board(board)
        position = int(input("Player 2's turn: "))
        board[position-10] = p2_mark
        display_board(board)
        
        check_condition()
        

game_input()    