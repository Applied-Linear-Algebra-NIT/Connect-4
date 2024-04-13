import numpy as np

BOARD_SIZE = 5

board = np.zeros((BOARD_SIZE, BOARD_SIZE))


def printBoard():
    for row in board:
        for cell in row:
            if cell == 0:
                print("⬜", end=" ")
            elif cell == 1:
                print("🔴", end=" ")
            elif cell == 2:
                print("🔵", end=" ")
        print()


def checkForWin(player):
    if np.any(np.sum(board == player, axis=1) >= 4):
        return True

    if np.any(np.sum(board == player, axis=0) >= 4):
        return True

    if np.any([np.sum(np.diag(board == player, k=i)) >= 4 for i in range(-board.shape[0]+4, board.shape[1]-3)]):
        return True

    if np.any([np.sum(np.diag(np.fliplr(board) == player, k=i)) >= 4 for i in range(-board.shape[0]+4, board.shape[1]-3)]):
        return True

    return False


def game():
    player = 1
    while True:
        printBoard()
        print("Player {}'s turn".format(player))
        while True:
            try:
                col = int(
                    input("Enter a column (0-{}): ".format(BOARD_SIZE - 1)))
                if 0 <= col < BOARD_SIZE:
                    break
            except ValueError:
                pass
        for row in range(BOARD_SIZE - 1, -1, -1):
            if board[row, col] == 0:
                board[row, col] = player
                if checkForWin(player):
                    printBoard()
                    print("Player {} wins!".format(player))
                    return
                player = 2 if player == 1 else 1
                break


game()
