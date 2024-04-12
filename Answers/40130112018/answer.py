import numpy as np


def showBoard(board):
    # for zero show ⚪ for player 1 show 🔴 and show 🔵 for player 2
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                print("⚪", end=" ")
            elif board[i][j] == 1:
                print("🔴", end=" ")
            else:
                print("🔵", end=" ")
        print()

    nums = ["1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ "]
    for i in range(5):
        print(nums[i], end=" ")


def play(board, col, player):
    for i in range(4, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            return True

    return False


def checkWin(board, player):
    # check horizontal
    for i in range(5):
        for j in range(2):
            if (
                board[i][j] == player
                and board[i][j + 1] == player
                and board[i][j + 2] == player
                and board[i][j + 3] == player
            ):
                return True

    # check vertical
    for i in range(2):
        for j in range(5):
            if (
                board[i][j] == player
                and board[i + 1][j] == player
                and board[i + 2][j] == player
                and board[i + 3][j] == player
            ):
                return True

    # check diagonal
    for i in range(2):
        for j in range(2):
            if (
                board[i][j] == player
                and board[i + 1][j + 1] == player
                and board[i + 2][j + 2] == player
                and board[i + 3][j + 3] == player
            ):
                return True

    for i in range(2):
        for j in range(4, 1, -1):
            if (
                board[i][j] == player
                and board[i + 1][j - 1] == player
                and board[i + 2][j - 2] == player
                and board[i + 3][j - 3] == player
            ):
                return True

    return False


# create a 5x5 board of zeros// 1 for player 1 and 2 for player 2
board = np.zeros((5, 5))

turn = True

while True:
    showBoard(board)
    if turn:
        print("Player 1's turn 🔴")
    else:
        print("Player 2's turn 🔵")

    try:
        col = int(input("Enter the column number: "))

        if col < 1 or col > 5:
            print("Please enter a valid number between 1 and 5")
            continue
    except:
        print("Please enter a valid number")
        continue

    if turn:
        res = play(board, col - 1, 1)
    else:
        res = play(board, col - 1, 2)
        
    if not res:
        print("Column is full select another column")
        continue

    turn = not turn

    if checkWin(board, 1):
        showBoard(board)
        print("Player 1 wins 🔴")
        break

    if checkWin(board, 2):
        showBoard(board)
        print("Player 2 wins 🔵")
        break
