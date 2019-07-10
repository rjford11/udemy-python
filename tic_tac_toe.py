#board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#player1 = ''
#player2 = ''
#playing = True

def replay():
    keep_playing = input('Do you wish to keep playing?')
    return keep_playing.upper() == 'YES'
    
def full_board_check(board):
    return ' ' in board
    
def space_check(board, position):
    return (board[position] != 'X' and board[position] != 'O')

import random
def choose_first():
  random_num = random.randint(1,2)
  print('Player {} went first.'.format(random_num))
  
def replay():
    pass

def win_check(board, marker):
    if ((marker in board[1] and marker in board[2] and marker in board[3])
     or (marker in board[1] and marker in board[4] and marker in board[7])
     or (marker in board[1] and marker in board[5] and marker in board[9])
     or (marker in board[2] and marker in board[5] and marker in board[8])
     or (marker in board[3] and marker in board[6] and marker in board[9])
     or (marker in board[4] and marker in board[5] and marker in board[6])
     or (marker in board[7] and marker in board[8] and marker in board[9])):
        print('Congratulations! GAME won by {}'.format(marker))
        playing = input('Would you like to play again?').lower()
        if (playing == 'yes'):
            board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            print_board(board)
            player_choice(board, marker)
        else:
            return False
    else:
        return True
    
def place_marker(board, marker, position):
    if (marker.upper() == 'X' or marker.upper() == 'O'):
        if (position < 1 or position > 9):
            print("Position must be between 1 and 9")
        board[position] = marker
        return board
    else:
        print('Marker must be X or O')
        
def check_position(position):
    if (board.count(position)) == 0:
        board[position] = position
    else:
        return 'fail'
    
def player_choice(board, marker):
    playing = True
    while playing:
        position = int(input("Choose your next position: (1-9)"))
        if (position < 1 or position > 9):
            print('The position must be between 1 and 9')

        check = space_check(board,position)
        if (check == False):
            print('SPACE Check playing {}'.format(check))
            print('This space is already taken.  Please choose a different space.')
            continue
        board = place_marker(board, marker, position)
        print_board(board)
        playing = win_check(board, marker)
        print('Playing = {}'.format(playing))
        if (marker == 'X'):
            marker = 'O'
        else:
            marker = 'X'

def player_input():
    while True:
        player1 = input("Player 1:  Do you want to be X or O?")
        player1 = player1.upper()
    
        if (player1 == 'X') or (player1 == 'O'):
            print()
            print('Player1 will go first.')
            break
        else:
            print('Please choose either X or O!')
      
    print('Are you ready to play? Enter Yes or No.')
    playing = input().lower()
    if playing == 'yes':
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        print()
        print()
        print_board(board)
        player_choice(board, player1)
    else:
        print("Why don't you want to play?")
        
from IPython.display import clear_output
def print_board(board):
    clear_output()
    line  = '   |   |\n'
    line2 = '  | '
    line3 = ' | '
    #patterns = {0:line +mylist[0] +line2 +mylist[1]+ line3 +mylist[2]+'\n'+line +'-----------\n' +line +mylist[3]+line2 +mylist[4] +line3 +mylist[5]+'\n' \
    #            +line +'-----------\n' +line +mylist[6] +line2 +mylist[7] +line3 +mylist[8] +'\n'+line}
    
    patterns = {0:line +board[1] +line2 +board[2]+ line3 +board[3]+'\n'+line +'-----------\n' +line +board[4]+line2 +board[5] +line3 +board[6]+'\n' \
                +line +'-----------\n' +line +board[7] +line2 +board[8] +line3 +board[9] +'\n'+line}
    
    for pattern in patterns:
        print(patterns[pattern])
    
print('Welcome to Tic Tac Toe!')
player_input()