#==== Global Variables

#Game Board
board=["-","-","-","-","-","-","-","-","-"]
#If game still running
game_still_going = True
#who won or tie
winner = None
#Whos turn is it
current_player="X"

def display_board():
    print(board[0] + " | "+ board[1] +" | " + board[2])
    print(board[3] + " | "+ board[4] +" | " + board[5])
    print(board[6] + " | "+ board[7] +" | " + board[8])

def play_game():
    display_board()
    #while game is still going
    while game_still_going:
        #handle single turn of player
        handle_turn(current_player)
        #check if the game has ended
        check_if_game_over()
        #Flip to other player
        flip_player()
        
        #The game has ended
        if winner == "X" or winner =="O":
            print(winner + " won.")
        elif winner == None:
            print("Tie.")


#handle a single turn of arbitary player
def handle_turn(player):
    
    print(player +"'s turn.")
    
    position = input ("Choose a position from 1-9: ")
    
    1
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position =input("Invalid input, choose a position from 1-9: ")
    
    position = int(position) -1
    
    if board[position] != "-":
        print("You can't go there. Go again.")
    
    board[position]= player
    
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #setup global variable
    global winner
    #check rows
    row_winner=check_rows()
    #check cols
    column_winner=check_columns()
    #check diagonals
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner = None
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #globalvariables we need
    global current_player
    #if current player x then change to o
    if current_player == "X":
        current_player = "O"
    #if current player o then change to x
    elif current_player == "O":
        current_player = "X"
    return

def check_rows():
    #setup global vars
    global game_still_going
    #check if all the rows are the same val and not empty
    row_1=board[0]==board[1]==board[2] != "-"
    row_2=board[3]==board[4]==board[5] != "-"
    row_3=board[6]==board[7]==board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #setup global vars
    global game_still_going
    #check if all the rows are the same val and not empty
    col_1=board[0]==board[3]==board[6] != "-"
    col_2=board[1]==board[4]==board[7] != "-"
    col_3=board[2]==board[5]==board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonals():
    #setup global vars
    global game_still_going
    #check if all the rows are the same val and not empty
    diagonal_1=board[0]==board[4]==board[8] != "-"
    diagonal_2=board[2]==board[4]==board[6] != "-"
    
    if diagonal_1 or diagonal_2:
        game_still_going=False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

play_game()