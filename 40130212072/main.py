import numpy as np
from colorama import init,Back

Row = 6
Col = 7
empty = 0
P1 = 1
P2 = 2
player_names = {P1: "First_player", P2: "Second_player"}


def create_board():
    return np.zeros((Row, Col), dtype=int)


def print_board(board):
    init(autoreset=True)
    for i in range(Row-1, -1, -1):
        for j in range(Col):
            if board[i][j] == empty:
                print(Back.BLACK + " | ", end="")
            elif board[i][j] == P1:
                print(Back.YELLOW + " | ", end="")
            else:
                print(Back.RED + " | ", end="")
        print(Back.RESET)


def location(board, col):
    return board[Row - 1][col] == empty


def find_empty_row(board, col):
    for i in range(Row):
        if board[i][col] == empty:
            return i


def insert_piece(board, row, col, piece):
    board[row][col] = piece


def move(board, piece):
    for i in range(Col - 3):
        for j in range(Row):
            if board[j][i] == piece and board[j][i + 1] == piece and board[j][i + 2] == piece and board[j][i + 3] == piece:
                return True
    for i in range(Col):
        for j in range(Row - 3):
            if board[j][i] == piece and board[j + 1][i] == piece and board[j + 2][i] == piece and board[j + 3][i] == piece:
                return True
    for i in range(Col - 3):
        for j in range(Row - 3):
            if board[j][i] == piece and board[j + 1][i + 1] == piece and board[j + 2][i + 2] == piece and board[j + 3][i + 3] == piece:
                return True
    for i in range(Col - 3):
        for j in range(3, Row):
            if board[j][i] == piece and board[j - 1][i + 1] == piece and board[j - 2][i + 2] == piece and board[j - 3][i + 3] == piece:
                return True
    return False


def play_game():
    while True:
        board = create_board()
        game_over = False
        turn = 1
        player1_piece = int(input("First_player: Choose your piece <1 or 2>: "))
        if player1_piece == P1:
            player2_piece = P2
            print(f"Second_player your piece is {player2_piece}")
        else:
            player2_piece = P1
            print(f"Second_player your piece is {player2_piece}")

        start_player = int(input("Who starts? First_player or Second_player <1 or 2> ?: "))
        print_board(board)

        while not game_over:
            if turn % 2 == start_player - 1:
                current_player = P1
            else:
                current_player = P2

            col = int(input("Make your selection <from 0 to 6>: "))
            if location(board, col):
                row = find_empty_row(board, col)
                insert_piece(board, row, col, current_player)
                if move(board, current_player):
                    print(f"{player_names[current_player]} wins!")
                    game_over = True
            else:
                print("column is full! choose another column.")
            print_board(board)
            if np.count_nonzero(board == empty) == 0:
                print("It's a tie!")
                game_over = True
            turn += 1

        play_again_input = input("Do you want to play again <yes or no> ?: ")
        if play_again_input.lower() == "yes":
            play_game()
        else:
            print("Bye Bye :)")
            break


play_game()
