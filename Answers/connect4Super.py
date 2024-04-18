import numpy as np
import pygame
import sys
import math
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7

def createBoard():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidPlace(board, col):
    return board[ROW_COUNT - 1][col] == 0

def openRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningCheck(board, piece):
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, WHITE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(
                    r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(
                    r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

def evaluate_board(board):
    score = 0
    # Check horizontal score
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r])]
        for c in range(COL_COUNT - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window)

    # Check vertical score
    for c in range(COL_COUNT):
        col_array = [int(board[r][c]) for r in range(ROW_COUNT)]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window)

    # Check positively sloped diagonal score
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window)

    # Check negatively sloped diagonal score
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += evaluate_window(window)

    return score

def evaluate_window(window):
    score = 0
    if window.count(2) == 4:
        score += 100  # AI wins
    elif window.count(2) == 3 and window.count(0) == 1:
        score += 5  # Three AI pieces and an empty cell
    elif window.count(2) == 2 and window.count(0) == 2:
        score += 2  # Two AI pieces and two empty cells
    if window.count(1) == 3 and window.count(0) == 1:
        score -= 4  # Three opponent pieces and an empty cell
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or winningCheck(board, 1) or winningCheck(board, 2):
        if winningCheck(board, 2):
            return (None, 100000000000000)
        elif winningCheck(board, 1):
            return (None, -10000000000000)
        else:
            return (None, evaluate_board(board))
    if maximizing_player:
        value = -math.inf
        column = random.choice([c for c in range(COL_COUNT) if isValidPlace(board, c)])
        for col in range(COL_COUNT):
            if isValidPlace(board, col):
                row = openRow(board, col)
                board_copy = board.copy()
                dropPiece(board_copy, row, col, 2)
                new_score = minimax(board_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return column, value
    else:
        value = math.inf
        column = random.choice([c for c in range(COL_COUNT) if isValidPlace(board, c)])
        for col in range(COL_COUNT):
            if isValidPlace(board, col):
                row = openRow(board, col)
                board_copy = board.copy()
                dropPiece(board_copy, row, col, 1)
                new_score = minimax(board_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return column, value

def ai_move(board):
    depth = 4  # You can adjust the depth of the search
    return minimax(board, depth, -math.inf, math.inf, True)[0]

def game_mode_selection_gui():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Welcome to Connect Four Game!")

    # Set up fonts
    font = pygame.font.SysFont(None, 30)

    # Menu options
    options = ["Single Player", "Two Players"]

    # Variable to hold the selected mode
    selected_mode = None

    # Main loop for the menu
    while True:
        screen.fill(WHITE)

        # Render and display the menu options
        for i, option in enumerate(options):
            text = font.render(option, True, BLACK)
            screen.blit(text, (150, 100 + i * 50))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a menu option was clicked
                x, y = pygame.mouse.get_pos()
                for i, _ in enumerate(options):
                    if 150 <= x <= 250 and 100 + i * 50 <= y <= 130 + i * 50:
                        selected_mode = i + 1

        # If a mode is selected, return it
        if selected_mode is not None:
            return selected_mode

        pygame.display.update()

# Get game mode selection
mode = game_mode_selection_gui()

# Create the game board
board = createBoard()

# Print the initial board
printBoard(board)

# Set up the game window
pygame.init()
SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

# Set up font
myfont = pygame.font.SysFont("monospace", 75)

# Game loop
gameOver = False
turn = 0

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if isValidPlace(board, col):
                    row = openRow(board, col)
                    dropPiece(board, row, col, 1)

                    if winningCheck(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        gameOver = True

            elif mode == 1:  # Single Player mode
                col = ai_move(board)

                if isValidPlace(board, col):
                    row = openRow(board, col)
                    dropPiece(board, row, col, 2)

                    if winningCheck(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        gameOver = True

            else:  # Two Players mode
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if isValidPlace(board, col):
                    row = openRow(board, col)
                    dropPiece(board, row, col, 2)

                    if winningCheck(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        gameOver = True

            printBoard(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if gameOver:
                pygame.time.wait(3000)
