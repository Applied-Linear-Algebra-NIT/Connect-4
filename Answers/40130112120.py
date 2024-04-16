import sys

import numpy as np


class Player:
    COLORS = ('r', 'b')

    def __init__(self, name, color, is_ai=False):
        if color not in self.COLORS:
            raise ValueError('Invalid color')
        self.name = name
        self.color = color
        self.wins = 0
        self.is_ai = is_ai

    def __str__(self):
        return self.name

    def won(self):
        self.wins += 1

    def __eq__(self, other):
        return self.color == other


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.p1 = player1
        self.p2 = player2
        self.player_turn = player1
        self.grid = np.full((5, 5), dtype='U', fill_value='N')
        self.last_completed_row = np.zeros((5,), dtype='i')

        self.start_game()

    def start_game(self):
        self.select_column(self.player_turn)

    def next_turn(self):
        if self.player_turn is self.p1:
            self.player_turn = self.p2
            return self.player_turn

        self.player_turn = self.p1
        return self.player_turn

    def select_column(self, player: Player, move=None):
        print('\n\n------------------------------------------------------------------')
        print(self.grid)

        if move is None:
            try:
                selected_col = int(input(f"{player}'s turn \nPlease Enter A Number From 1 to 5: "))
                while selected_col > 5 or selected_col < 1:
                    selected_col = int(input('Invalid Entry\nPlease Enter A Number From 1 to 5: '))
            except ValueError:
                self.select_column(player, None)

            selected_col -= 1

            if self.last_completed_row[selected_col] == 5:
                print(f'Column {selected_col} Is Completed \nPlease Select Again!\n')
                return self.select_column(player, None)
        else:
            selected_col = move

        row = 4 - self.last_completed_row[selected_col]
        self.last_completed_row[selected_col] += 1
        self.grid[row, selected_col] = player.color

        won = self.check(selected_col, row)
        if won:
            player.wins += 1
            print(f'\n\n{player.name} HAS WON!!!\n' +
                  'Have A Nice Day\n' +
                  'Goodbye')
            sys.exit()

        player = self.next_turn()
        next_move = None
        if player.is_ai:
            columns = [col for col in range(5) if self.last_completed_row[col] != 5]

            next_move = np.random.choice(columns, size=1)
        self.select_column(player, next_move)

    def check(self, col, row):
        if (
                self._check_vertical(col, row)
                # self._check_horizontal(col, row) or
                # self._check_left_diagonal(col, row) or
                # self._check_right_diagonal(col, row)
        ):
            return True
        return False

    def _check_vertical(self, col, row):
        p = self.player_turn
        row = row + 1
        num = 1
        while row < 5:
            if self.grid[row, col] != p:
                break
            num += 1
            row += 1

        return num >= 4

    def _check_horizontal(self, col, row):
        p = self.player_turn
        num = 1
        left_col = col - 1
        right_col = col + 1
        while left_col >= 0:
            if self.grid[row, left_col] != p:
                break
            left_col -= 1
            num += 1

        while right_col < 5:
            if self.grid[row, right_col] != p:
                break
            right_col += 1
            num += 1

        return num >= 4

    def _check_right_diagonal(self, col, row):
        p = self.player_turn
        num = 1
        upper_right = (row - 1, col + 1)
        lower_left = (row + 1, col - 1)

        row, col = upper_right
        while row >= 0 and col < 5:
            if self.grid[row, col] != p:
                break
            row -= 1
            col += 1
            num += 1

        row, col = lower_left
        while row < 5 and col >= 0:
            if self.grid[row, col] != p:
                break
            row += 1
            col -= 1
            num += 1

        return num >= 4

    def _check_left_diagonal(self, col, row):
        p = self.player_turn
        num = 1
        upper_left = (row - 1, col - 1)
        lower_right = (row + 1, col + 1)

        row, col = upper_left
        while row >= 0 and col >= 0:
            if self.grid[row, col] != p:
                break
            row -= 1
            col -= 1
            num += 1

        row, col = lower_right
        while row < 5 and col < 5:
            if self.grid[row, col] != p:
                break
            row += 1
            col += 1
            num += 1

        return num >= 4


choice = int(input('Please Choose The Game Mode:\n' +
                   '1. Single Player\n' +
                   '2. Multiplayer\n' +
                   '3. Exit\n' +
                   '> '))

if choice == 1:
    name = input('Enter Your Name: ')
    p1 = Player(name, 'r')
    p2 = Player('Computer', 'b', is_ai=True)
elif choice == 2:
    print('First Player')
    name = input('Enter Your Name: ')
    print('Second Player')
    p1 = Player(name, 'r')
    name = input('Enter Your Name: ')
    p2 = Player(name, 'b')
else:
    sys.exit()

game = Game(p1, p2)
