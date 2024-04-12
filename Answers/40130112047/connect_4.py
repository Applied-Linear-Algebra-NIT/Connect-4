import numpy as np

p1_win = False
p2_win = False

positions = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])

p1_positions = []
p2_positions = []

turn = "p1"

def check_win():
    check_win_1()
    check_win_2()

def check_win_1():
    global p1_win

    for i in p1_positions:
        if ((len(positions[i[0]-3:i[0]+1, i[1]])==4)and(np.all(positions[i[0]-3:i[0]+1, i[1]]==1)))\
        or ((len(positions[i[0]-2:i[0]+2, i[1]])==4)and(np.all(positions[i[0]-2:i[0]+2, i[1]]==1))) or\
        ((len(positions[i[0]-1:i[0]+3, i[1]])==4)and(np.all(positions[i[0]-1:i[0]+3, i[1]]==1)))\
        or ((len(positions[i[0]:i[0]+4, i[1]])==4)and(np.all(positions[i[0]:i[0]+4, i[1]]==1))):
            p1_win=True
            break

        elif ((len(positions[i[0], i[1]-3:i[1]+1])==4)and(np.all(positions[i[0], i[1]-3:i[1]+1]==1)))\
        or ((len(positions[i[0], i[1]-2:i[1]+2])==4)and(np.all(positions[i[0], i[1]-2:i[1]+2]==1))) or\
        ((len(positions[i[0], i[1]-1:i[1]+3])==4)and(np.all(positions[i[0], i[1]-1:i[1]+3]==1)))\
        or ((len(positions[i[0], i[1]:i[1]+4])==4)and(np.all(positions[i[0], i[1]:i[1]+4]==1))):
            p1_win=True
            break

        else:
            if np.all(positions.diagonal(1)==1):
                p1_win=True
                break
            elif np.all(positions.diagonal(-1)==1):
                p1_win=True
                break
            elif np.all(np.flipud(positions).diagonal(1)==1):
                p1_win=True
                break
            elif np.all(np.flipud(positions).diagonal(-1)==1):
                p1_win=True
                break
            elif np.count_nonzero(positions.diagonal(0)==1)==4:
                p1_win=True
                break
            elif np.count_nonzero(np.flipud(positions).diagonal(0)==1)==4:
                p1_win=True
                break




def check_win_2():
    global p2_win

    for i in p2_positions:
        if ((len(positions[i[0]-3:i[0]+1, i[1]])==4)and(np.all(positions[i[0]-3:i[0]+1, i[1]]==2)))\
        or ((len(positions[i[0]-2:i[0]+2, i[1]])==4)and(np.all(positions[i[0]-2:i[0]+2, i[1]]==2))) or\
        ((len(positions[i[0]-1:i[0]+3, i[1]])==4)and(np.all(positions[i[0]-1:i[0]+3, i[1]]==2)))\
        or ((len(positions[i[0]:i[0]+4, i[1]])==4)and(np.all(positions[i[0]:i[0]+4, i[1]]==2))):
            p2_win=True
            break

        elif ((len(positions[i[0], i[1]-3:i[1]+1])==4)and(np.all(positions[i[0], i[1]-3:i[1]+1]==2)))\
        or ((len(positions[i[0], i[1]-2:i[1]+2])==4)and(np.all(positions[i[0], i[1]-2:i[1]+2]==2))) or\
        ((len(positions[i[0], i[1]-1:i[1]+3])==4)and(np.all(positions[i[0], i[1]-1:i[1]+3]==2)))\
        or ((len(positions[i[0], i[1]:i[1]+4])==4)and(np.all(positions[i[0], i[1]:i[1]+4]==2))):
            p2_win=True
            break
        
        else:
            if np.all(positions.diagonal(1)==2):
                p2_win=True
                break
            elif np.all(positions.diagonal(-1)==2):
                p2_win=True
                break
            elif np.all(np.flipud(positions).diagonal(1)==2):
                p2_win=True
                break
            elif np.all(np.flipud(positions).diagonal(-1)==2):
                p2_win=True
                break
            elif np.count_nonzero(positions.diagonal(0)==2)==4:
                p2_win=True
                break
            elif np.count_nonzero(np.flipud(positions).diagonal(0)==2)==4:
                p2_win=True
                break
                
        

while p1_win!=True and p2_win!=True:

    if turn=="p1":
        while 1:
            print("\n_Player 1:")
            x = int(input("Print X of your point: "))
            y = int(input("Print Y of your point: "))

            if (x<0 or x>4):
                print("sorry your X is not in the allowed coordinates")
            elif (y<0 or y>4):
                print("sorry your Y is not in the allowed coordinates")
            elif ([x,y] in p1_positions) or ([x,y] in p2_positions):
                print("sorry this point is already used")
            else:
                t = False
                try :
                    if (y>0 and positions[x+1][y]==0):
                        t=True
                except Exception as e:
                    print(e)
                if t:
                    print("Sorry this point is not allowed")
                else:
                    break
        
        p1_positions.append([x,y])
        positions[x][y]=1
        turn="p2"

        print(positions)
    
    check_win()
    if p1_win:
        print("Player 1 won the game")
        break
    if p2_win:
        print("Player 2 won the game")
        break

    
    if turn=="p2":
        while 1:
            print("\n_Player 2:")
            x = int(input("Print X of your point: "))
            y = int(input("Print Y of your point: "))

            if (x<0 or x>4):
                print("sorry your X is not in the allowed coordinates")
            elif (y<0 or y>4):
                print("sorry your Y is not in the allowed coordinates")
            elif ([x,y] in p1_positions) or ([x,y] in p2_positions):
                print("sorry this point is already used")
            else:
                t = False
                try :
                    if (y>0 and positions[x+1][y]==0):
                        t=True
                except Exception as e:
                    print(e)
                if t:
                    print("Sorry this point is not allowed")
                else:
                    break

        
        p2_positions.append([x,y])
        positions[x][y]=2
        turn="p1"

        print(positions)
    
    check_win()

    if p1_win:
        print("Player 1 won the game")
        break
    if p2_win:
        print("Player 2 won the game")
        break