import  numpy as np
#size
Row=5
Column=5

#creating board with numpy
def CreateBoard():
    return np.zeros((Row,Column), "int32")


def getNextRow(board, col):
    for row in range(Row-1, -1, -1):
        if board[row][col] == 0:
            return row

#check if column is full
def CheckCol(board,col):
    return board[0][col] == 0


#Add piece
def PutPiece(board,row,col,player):
    board[row][col] = player

#check if there is a winner
def CheckwinnerMove(board,player):
    for col in range(Column - 3):
        for row in range(Row):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    for col in range(Column):
        for row in range(Row - 3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    for col in range(Column- 3):
        for row in range(Row- 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    for col in range(Column- 3):
        for row in range(3, Row):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and  board[row - 3][col + 3] == player:
                return True

#start of game
def game(board,turn,gameplay):
  while  gameplay:
     print(board)
     if turn==0:
        col= int(input("Player1's turn:"))
        if CheckCol(board,col):
            row=getNextRow(board,col)
            PutPiece(board,row,col,1)
            if CheckwinnerMove(board,1):
              print("Player1 won the game :)")
              gameplay=False
        else:
             print("That column is already filled!")
             game(board,turn,gameplay)
     elif turn==1:
         col = int(input("Player2's turn:"))
         if CheckCol(board,col):
             row = getNextRow(board, col)
             PutPiece(board, row, col, 2)
             if CheckwinnerMove(board, 2):
              print("Player2 won the game :)")
              gameplay=False
         else:
             print("That column is already filled!")
             game(board, turn, gameplay)

     turn=(turn+1)%2


board=CreateBoard()
turn=0
gameplay=True
game(board,turn,gameplay)