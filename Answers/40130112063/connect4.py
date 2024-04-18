import numpy as np


rows = 5
cols = 5


def create_board():
    board = np.zeros((rows, cols), dtype=int)
    return board


def is_column_free(board, col):
    return board[rows - 1, col] == 0


def drop_piece(board, col, player):
    for row in range(rows - 1, -1, -1):
        if board[row, col] == 0:
            board[row, col] = player
            break


def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print("|  ", end="")
            elif cell == 1:
                print("| X ", end="")
            else:
                print("| O ", end="")
        print("|")


def check_win(board, player):
    # check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if (board[row, col] == player and
                    board[row, col + 1] == player and
                    board[row, col + 2] == player and
                    board[row, col + 3] == player):
                return True

    # check vertical
    for col in range(cols):
        for row in range(rows - 3):
            if (board[row, col] == player and
                    board[row + 1, col] == player and
                    board[row + 2, col] == player and
                    board[row + 3, col] == player):
                return True

    # Check both diagonals
    for col in range(cols - 3):
        for row in range(rows - 3):
            if (board[row, col] == player and
                    board[row + 1, col + 1] == player and
                    board[row + 2, col + 2] == player and
                    board[row + 3, col + 3] == player):
                return True

    for col in range(3, cols):
        for row in range(rows - 3):
            if (board[row, col] == player and
                    board[row + 1, col - 1] == player and
                    board[row + 2, col - 2] == player and
                    board[row + 3, col - 3] == player):
                return True

    return False


def is_board_full(board):
    return board[0].all() != 0


def game():

    board = create_board()
    current_player = 1  # Player 1 starts

    while True:
        print_board(board)

        while True:
            try:
                col = int(input(f"Player {current_player}, choose a number between 1 to 5: ")) - 1
                if 0 <= col < cols and (board, col):
                    break
                else:
                    print("Invalid number. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 5")

        drop_piece(board, col, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Tie!")
            break

        current_player = current_player % 2 + 1


game()
