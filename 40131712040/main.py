import numpy as np

ROWS = 6
COLUMNS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
PLAYER_NAMES = {
    PLAYER1: "Player 1",
    PLAYER2: "Player 2"
}


def design_board(board):
    for r in range(6 - 1, -1, -1):
        for c in range(6):
            if board[r][c] == EMPTY:
                print("\033[1;39;40m✖", end=" ")
            elif board[r][c] == PLAYER1:
                print("\033[1;32;40m✖", end=" ")
            else:
                print("\033[1;31;40m✖", end=" ")
        print("\033[1;39;40m✖")
    print("\033[1;39;40m" + "------------------------------")


def location(board, col):
    return board[ROWS - 1][col] == EMPTY


def find_empty_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r


def insert(board, row, col, piece):
    board[row][col] = piece


def player_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False


def game():
    play_again = True

    while play_again:
        # Create a new game board
        board_state = np.zeros((6, 7), dtype=int)
        design_board(board_state)
        game_over = False
        turn = 0
        # Determine starting player
        starting_player = int(input("Who starts? (1 or 2): "))

        player_color_choice = int(input(f"{PLAYER_NAMES[PLAYER1]}, choose your color (1: RED , 2: GREEN): "))
        if player_color_choice == 1:
            PLAYER1_COLOR = "\033[1;31;40m"  # Red
            PLAYER2_COLOR = "\033[1;32;40m"  # Green
        else:
            PLAYER1_COLOR = "\033[1;32;40m"  # Green
            PLAYER2_COLOR = "\033[1;31;40m"  # Red

        print("   START   ")

        while not game_over:
            # Player 1's turn
            if turn % 2 == starting_player - 1:
                current_player = PLAYER1
                current_color = PLAYER1_COLOR
            # Player 2's turn
            else:
                current_player = PLAYER2
                current_color = PLAYER2_COLOR

            print(f"{current_color}{PLAYER_NAMES[current_player]}'s turn")

            col = int(input("Make your selection (0-6): "))
            if location(board_state, col):
                row = find_empty_row(board_state, col)
                insert(board_state, row, col, current_player)

                if player_move(board_state, current_player):
                    print(f"{PLAYER_NAMES[current_player]} wins!")
                    game_over = True
            else:
                print("Column is full. Choose another column.")

            design_board(board_state)

            # If the board is full
            if np.count_nonzero(board_state == EMPTY) == 0:
                print("It's a tie!")
                game_over = True

            turn += 1

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"


# Start the game
game()