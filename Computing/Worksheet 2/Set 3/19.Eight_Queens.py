#Recursive Solution
def no_attack(board,col,row):
    for i in range(col):# checking adjacent cells
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):# checking upper diagonal
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,8,1), range(col,-1,-1)):# checking lower diagonal
        if board[i][j] == 1:
            return False
    return True

def place_queens(board,col):
    if col >=8:# base case - all queens are placed
        return True

    for i in range(8):
        if no_attack(board,col,i):
            board[i][col] = 1

            if place_queens(board,col+1):
                return True
            else:
                board[i][col] = 0
    return False # if 8 queens can't be placed return false

def print_board(board):
    for i in range(8):
        for j in range(8):
            print (board[i][j],end=" ")
        print ("")

def main():
    board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

    if place_queens(board,0):
        print("Yes")
    else:
        print("No")
    print_board(board)
main()

