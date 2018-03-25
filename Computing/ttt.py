# Tic Tac Toe Representation:

#      |     |
#  x_0 | x_1 | x_2
#      |     |
# -----------------
#      |     |
#  x_3 | x_4 | x_5
#      |     |
# -----------------
#      |     |
#  x_6 | x_7 | x_8
#      |     |

# board = [[x_0, x_1, x_2], [x_3, x_4, x_5], [x_6, x_7, x_8]]



# function to print the board
# expects board representation specified above
def print_board(board):
    # row 1
    print("   |   |")
    print(" " + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]))
    print("   |   |")
    print("------------")
    # row 2
    print("   |   |")
    print(" " + str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]))
    print("   |   |")
    print("------------")
    # row 3
    print("   |   |")
    print(" " + str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]))
    print("   |   |")



# function to get user input for move
# assumes that it will only be called when the game has not ended
def get_player_move(board, turn):
    # determine whose turn it is
    if turn % 2:
        player = "1"
    else:
        player = "2"

    valid_move = False
    while not valid_move:
        print("Player " + player + "'s move.")
        input_row = int(input("Please select a row to play on (0, 1, 2): "))
        input_col = int(input("Please select a column to play on (0, 1, 2): "))
        if board[input_row][input_col] == 0:
            return (input_row, input_col)
        else:
            print("Invalid row-column selection! Square is already filled!")



# function to update the board with a valid move
# expects move to be the tuple: (input_row, input_col)
def update_board(board, move, turn):
    if turn % 2:
        board[move[0]][move[1]] = 1
    else:
        board[move[0]][move[1]] = 2
    return board



# function to check that the board isn't full
def board_full(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    # else board is full
    return True



# function to check for a winning state
def check_winner(board):
    # get all the sequences to check
    sequences = []
    sequences.append(board[0]) # row 0
    sequences.append(board[1]) # row 1
    sequences.append(board[2]) # row 2
    sequences.append([board[0][0], board[1][0], board[2][0]]) # col 0
    sequences.append([board[0][1], board[1][1], board[2][1]]) # col 1
    sequences.append([board[0][2], board[1][2], board[2][2]]) # col 2
    sequences.append([board[0][0], board[1][1], board[2][2]]) # diag 0
    sequences.append([board[0][2], board[1][1], board[2][0]]) # diag 1
    # the game can still be won if at least 1 sequence
    # - i.e., row/col/diag - does not contain moves made by both players
    for i in range(len(sequences)):
        if sequences[i][0] == sequences[i][1] == sequences[i][2] and sequences[i][0] != 0:
            return sequences[i][0]
    # else no winner
    return 0



# function to check if the game can still be won
def check_winnable(board):
    # get all the sequences to check
    sequences = []
    sequences.append(board[0]) # row 0
    sequences.append(board[1]) # row 1
    sequences.append(board[2]) # row 2
    sequences.append([board[0][0], board[1][0], board[2][0]]) # col 0
    sequences.append([board[0][1], board[1][1], board[2][1]]) # col 1
    sequences.append([board[0][2], board[1][2], board[2][2]]) # col 2
    sequences.append([board[0][0], board[1][1], board[2][2]]) # diag 0
    sequences.append([board[0][2], board[1][1], board[2][0]]) # diag 1
    # the game can still be won if at least 1 sequence
    # - i.e., row/col/diag - does not contain moves made by both players
    for i in range(len(sequences)):
        if not (1 in sequences[i] and 2 in sequences[i]):
            return True
    # else not winnable
    return False






# main game loop
play_ttt = True
while play_ttt:
    
    # determine if players want to continue playing or quit
    selection = input("\n\nPlease press \"P\" to Play or \"X\" to Exit: ")

    if selection not in ["X", "x", "P", "p"]:
        print("Invalid input! Please only select \"P\" or \"X\".")

    elif selection in ["P", "p"]:
        # initialise game variables
        turn = 0
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # loop the game until it ends
        while check_winnable(board) and (not check_winner(board)):
            turn += 1
            print_board(board)
            board = update_board(board, get_player_move(board, turn), turn)

        # determine game outcome
        print_board(board)
        winner = check_winner(board)
        if winner:
            print("Player " + str(winner) + " has won!!!")
        elif not check_winnable(board):
            print("The game is a draw!!!")
        
    elif selection in ["X", "x"]:
        play_ttt = False
