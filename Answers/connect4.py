import os

board_x = 5
board_y = 5
line = '|'
empty = ' '
player_icon = ["X","O"]

board = [[empty for i in range(board_y)] for i in range(board_x)]

def draw(board):
    os.system('cls' if os.name=='nt' else 'clear')
    print('',end=" ")
    for i in range(5):
        print(i+1, end=" ")
    print()

    for i in range(board_y):
        print('|',end="")
        for j in range(board_x):
            print(f"{board[i][j]}|",end="")
        print()

#functions inside game()

def get_player_move(icon, board_x):
    while True:    
        try:
            move = int(input(f"\n\nit's {icon}'s turn! please choose a column: ")) - 1
            if move < 0 or move > board_x:
                raise Exception
            return move
        except:
            pass

def action(move, icon, board, board_x):
    global empty
    for i in reversed(range(board_x)):
        if board[i][move] == empty:
            board[i][move] = icon
            return True
    return False


def check_up(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_up(i-1, j, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_up_right(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_up_right(i-1, j+1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_right(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_right(i, j+1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_down_right(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_down_right(i+1, j+1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_down(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_down(i+1, j, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_down_left(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_down_left(i+1, j-1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_left(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_left(i, j-1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_up_left(i, j, board, count, icon):
    try:
        if board[i][j] == icon and count == 0:
            return True
        elif board[i][j] == icon:
            return check_up_left(i-1, j-1, board, count-1, icon)
        else:
            return False
    except:
        return False


def check_if_player_won(board, icon):
    count = 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            if  board[i][j] == icon and ( check_up(i-1, j, board, count, icon)
                                          or check_up_right(i-1, j+1, board, count, icon) 
                                          or check_right(i, j+1, board, count, icon) 
                                          or check_down_right(i+1, j+1, board, count, icon) 
                                          or check_down(i+1, j, board, count, icon) 
                                          or check_down_left(i+1, j-1, board, count, icon) 
                                          or check_left(i, j-1, board, count, icon) 
                                          or check_up_left(i-1, j-1, board, count, icon)):
                return True
    return False

def game(player_icon, board):
    turn = 0
    while True:
        draw(board)
        if check_if_player_won(board,player_icon[turn]):
            return turn

        #swap the turn
        turn=0 if turn else 1
        
        allGood = False
        while allGood is False:
            move = get_player_move(player_icon[turn], board_x)
            allGood = action(move, player_icon[turn], board, board_x)

print(game(player_icon, board))