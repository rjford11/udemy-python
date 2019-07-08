board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''
playing = True

def replay():
    pass
	
def check_position(position):
    if (board.count(position)) == 0:
        board[position] = position
	else:
		return 'fail'
    
def play_game():
    while playing:
        position = int(input("Choose your next position: (1-9"))
		check = check_position(position)
		if (check == 'fail'):
		    print('This position has already been used.  Please pick a different position.")
		
		playing = False
        
def start_game():
    print('Welcome to Tic Tac Toe!')
    print()
    player1 = input("Player 1:  Do you want to be X or O?")
    player1 = player1.upper()
    print('player1 = ' +player1)
    #return player !='X' or player !='O'
    if (player1 == 'X') or (player1 == 'O'):
        print('Player1 will go first.')
    else:
        print('Please choose either X or O!')
        return False
        
    print()
    print('Are you ready to play? Enter Yes or No.')
    playing = input().lower()
    if playing == 'yes':
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        print()
        print_board(board)
    else:
        "Why don't you want to play?"
        
def print_board(board):
    #mylist = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #mylist[num-1] = player
    #if init != 'yes':
     #   board[num] = player
    line  = '   |   |\n'
    line2 = '  | '
    line3 = ' | '
    
    #patterns = {0:line +mylist[0] +line2 +mylist[1]+ line3 +mylist[2]+'\n'+line +'-----------\n' +line +mylist[3]+line2 +mylist[4] +line3 +mylist[5]+'\n' \
    #            +line +'-----------\n' +line +mylist[6] +line2 +mylist[7] +line3 +mylist[8] +'\n'+line}
    
    patterns = {0:line +board[0] +line2 +board[1]+ line3 +board[2]+'\n'+line +'-----------\n' +line +board[3]+line2 +board[4] +line3 +board[5]+'\n' \
                +line +'-----------\n' +line +board[6] +line2 +board[7] +line3 +board[8] +'\n'+line}
    
    for pattern in patterns:
        print(patterns[pattern])