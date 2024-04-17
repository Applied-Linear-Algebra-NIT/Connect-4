import numpy as np

def start_game(player_names):

    def player_input_validation(c_index, tc_index):
        while True:
            if c_index.isdigit():
                c_index = int(c_index)
                while True:
                    i = c_index - 1
                    if c_index<1 or c_index>5:
                        c_index = int(input("Invalid input! please try again : "))
                    elif tc_index[i] == 0:
                        c_index = int(input("This column is already filled! Please choose another column : "))
                    else:
                        return c_index
            else:
                c_index = input("Please enter a \"number\" : ")
    
    def table_check(table, tc_index):

        c = np.min(tc_index)
        # horizontal check
        for t in range(-1, c-6, -1):
            row = table[t]
            for i in range(2):
                if np.all(row[i:i+4] == row[i:i+4][0]) and row[i]!=0:
                    return row[i]
        
        # vertical & diagonal check
        if c<2:
            # vertical check
            for j in range(5):
                column = table[:, j]
                for i in range(2):
                    if np.all(column[i:i+4] == column[i]) and column[i] != 0:
                        return column[i]
            
            # diagonal check
            for j in range(-1, 2, 1):
                # ltr
                diagonal_ltr = np.diag(table, k=j)
                # rtl
                diagonal_rtl = np.diag(np.fliplr(table), k=j)
                for p in range(2):
                    diagonal = diagonal_ltr if p==0 else diagonal_rtl                    
                    if j==0:
                        for i in range(2):
                            if np.all(diagonal[i:i+4] == diagonal[i:i+4][0]) and diagonal[i]!=0:
                                return diagonal[i]
                    else:
                        if np.all(diagonal[0:4] == diagonal[0:4][0]) and diagonal[i]!=0:
                            return diagonal[i]
                
        return 0
    
    table = np.zeros((5, 5), dtype=int)
    tc_index = np.full(5, 5, dtype=int)
    print(table)

    c = 0

    while True:
        c+=1
        odd = c%2

        # players' turns
        if odd == 1:
            column_index = player_input_validation(input(f"\n{player_names[0]}'s turn : "), tc_index)
        elif odd == 0:
            column_index = player_input_validation(input(f"\n{player_names[1]}'s turn : "), tc_index)
            odd+=2
        
        # change in table
        j = column_index - 1
        tc_index[j] -= 1
        table[tc_index[j], j] = odd

        print((f"{table}"))
        
        # check for 4 connections
        r = table_check(table, tc_index)
        if r==1:
            print(f"\n{player_names[0]} wins the Game, Congratulations.")
            return 0
        elif r==2:
            print(f"\n{player_names[1]} wins the Game, Congratulations.")
            return 0
        
        # check if the table is completely filled
        if np.all(tc_index == 0):
            print("\nThe game ended with a draw. We have no winner.")
            return 0
    
    return 0

def player_names():
    def player_name_validation(string):
        while True:
            if len(string.strip()) == 0:
                string = input("You must enter your name to play the Game : ")
            else:
                return string
    
    player_names = np.array([])

    player_names = np.append(player_names, player_name_validation(str(input("\nEnter your name as Player 1 :"))))
    player_names = np.append(player_names, player_name_validation(str(input("Enter your name as Player 2 :"))))

    print(player_names)
    print(f"\nDear {player_names[0]}, the number of \"1\" is your sign in the Game board.\nDear {player_names[1]}, the number of \"2\" is your sign in the Game board.\n")

    start_game(player_names)

    return 0

def lobby():
    def lobby_input_validation(num, initial):
        if num==0:
            while initial != "y" and initial != "n":
                initial = input("\nInvalid input!\nWould you like to play? (y/n)")
            return initial
        elif num==1:
            while initial != "y" and initial != "n":
                initial = input("\nInvalid input!\nWould you like to play AGAIN? (y/n)")
            return initial
        
    initial = lobby_input_validation(0, input("Would you like to play? (y/n)"))

    if initial=="y":
        while True:
            player_names()

            initial = lobby_input_validation(1, input("Would you like to play AGAIN? (y/n)"))
            if initial=="n":
                print("\nAlright then, have a nice time.")
                return 0
        
    elif initial=="n":
        print("\nAlright then, have a nice time.")
    
    return 0

lobby()
