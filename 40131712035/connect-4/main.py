import numpy as np

grid = np.zeros((5, 5), dtype=int)

player1 = 1
player2 = 2
currentPlayer = player1


def welcome():
    print("Welcome to Connect-4!\n", "Choose the mode you want to play:\n", "1.Multiplayer\n", "2.Single Player\n",
          "Enter 1 or 2:")
    mode = int(input())
    print("Start...")
    print("----------------------------")
    return mode


def display_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()


def is_column_full(col):
    return grid[0, col] != 0


def place_disc(col):
    for row in range(4, -1, -1):
        if grid[row, col] == 0:
            grid[row, col] = currentPlayer
            break


def check_winner():
    for row in range(5):
        for col in range(2):
            if grid[row, col] == currentPlayer and grid[row, col + 1] == currentPlayer and grid[row, col + 2] == currentPlayer and grid[row, col + 3] == currentPlayer:
                return True

    for row in range(2):
        for col in range(5):
            if grid[row, col] == currentPlayer and grid[row + 1, col] == currentPlayer and grid[row + 2, col] == currentPlayer and grid[row + 3, col] == currentPlayer:
                return True

    for row in range(2):
        for col in range(2):
            if grid[row, col] == currentPlayer and grid[row + 1, col + 1] == currentPlayer and grid[row + 2, col + 2] == currentPlayer and grid[row + 3, col + 3] == currentPlayer:
                return True

    for row in range(2):
        for col in range(3, 5):
            if grid[row, col] == currentPlayer and grid[row + 1, col - 1] == currentPlayer and grid[row + 2, col - 2] == currentPlayer and grid[row + 3, col - 3] == currentPlayer:
                return True

    return False


def get_player_move():
    while True:
        col = int(input(f"Player {currentPlayer}, choose a column (0-4): "))
        if not (0 <= col < 5):
            print("Invalid column. Please choose a column between 0 and 4.")
            continue
        if is_column_full(col):
            print("Column is full. Please choose another column.")
            continue
        return col


while True:
    mode = welcome()
    while True:
        if mode == 1:
            display_grid()
            col = get_player_move()
            place_disc(col)
            if check_winner():
                display_grid()
                print(f"Player {currentPlayer} wins!")
                break
            currentPlayer = player2 if currentPlayer == player1 else player1
        else:
            display_grid()
            if currentPlayer == player1:
                col = get_player_move()
            else:
                available_columns = [c for c in range(5) if not is_column_full(c)]
                col = np.random.choice(available_columns)
                print(f"AI Player chooses column {col}")
            place_disc(col)
            if check_winner():
                display_grid()
                print(f"Player {currentPlayer} wins!")
                break
            currentPlayer = player2 if currentPlayer == player1 else player1
    again = input("Do you want to play again?(y/n)")
    if again == "n":
        print("Have a nice day!")
        exit()
