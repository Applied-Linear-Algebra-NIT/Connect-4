import numpy as np

row_count = 5
col_count = 5

def create_board():
    board = np.zeros((5, 5))
    return board

def print_board(board):
    print(np.flip(board, 0))

def add_to_board(board, row, col, player):
    board[row][col] = player

def is_location_valid(board, row, col):
    if board[row][col] == 0:
        return True
    else:
        print("Pick another location!")
        return False

def winning_move(board, player, flag):
    check = 0

    # horizontally
    for r in range(row_count):
        for c in range(col_count):
            if board[r][c] == player:
                check += 1
        if check == 5:
            print(f'Player{player} has won')
            flag = False
            return flag
        else:
            check = 0

    # vertically
    for c in range(col_count):
        for r in range(row_count):
            if board[r][c] == player:
                check += 1
        if check == 5:
            print(f'Player{player} has won')
            flag = False
            return flag
        else:
            check = 0

    for r in range(row_count):
        if board[r][r] == player:
            check += 1
    if check == 5:
        print(f'Player{player} has won')
        flag = False
        return flag

    return flag

def available_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def player1(board):
    col = int(input("Player1 pick your column from 0-4 : "))
    row = available_row(board, col)

    if is_location_valid(board, row, col):
        add_to_board(board, row, col, 1)
    else:
        player1(board)

def player2(board):
    col = int(input("Player2 pick your column from 0-4 : "))
    row = available_row(board, col)

    if is_location_valid(board, row, col):
        add_to_board(board, row, col, 2)
    else:
        player2(board)

def gameplay(turn):
    flag = True
    board = create_board()
    print_board(board)

    while flag:
        if turn % 2 == 0:
            player1(board)
            flag = winning_move(board, 1, flag)
        else:
            player2(board)
            flag = winning_move(board, 2, flag)

        turn += 1

        if turn == 25:
            print("Game over!")
            flag = False

        print(board)



turn = 0
gameplay(turn)


