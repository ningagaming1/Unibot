import os
import time

board = [
    ["0","0","0"],
    ["0","0","0"],
    ["0","0","0"]
]

player = ["X","O"]
timer_tulip = (25,10)

#-------main_game------
def tic_tac_toe():
    playing = True
    p=0 #timer conter move+=1 every time a turn is taken

    #startup animation
    for i in range(3):
        for j in range(3):
            banner()
            display_board()
            board[i][j]=" "
            time.sleep(0.2)
            clear()

    while playing:

        #presenting display
        banner()
        display_board()
        
        if board_full():
            timer = timer_tulip[1]
            for i in range(timer_tulip[1]):
                print("board is full")
                print("closing game in")
                timer-=1
                print(f"{timer}sec")
                time.sleep(1)
            playing = False

        current_player = player[p%2]
        try:
            #taking input and spliting given input with proper index
            cord_in = input("enter move [as row coloum]:")
            cords = list(map(int,cord_in.split(" ")))
            i,j = cords[0],cords[1]
            #cheaking if the move is valid
            if valid(i,j):
                board[i][j]=current_player
                clear()
                p+=1
                #checks if the player has won and stops if a playe has won
                if win_check(current_player):
                    timer = timer_tulip[0]
                    #reseting the board
                    for i in range(timer_tulip[0]):
                        clear()
                        print(f"player-{current_player} has won")
                        display_board()
                        timer-=1
                        print(f"restarting in {timer} seconds")
                        time.sleep(1)
                    playing = False
                
                clear()
        #prevents error if input out of index
        except IndexError:
            clear()
            print("number out of range")
        #prevent error if a sting value is taken in as error
        except ValueError:
            clear()
            print("invalid input")

#mini fuctions for the main game
def banner():
    print("-"*37)
    print(" "*10+"Tic_Tac_toe")
    print("❌ --- Tic-Tac-Toe (1v1 Local) --- ⭕")
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def display_board():
    print("  0   1   2 ")
    print(f"0 {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f" ---|---|---")
    print(f"1 {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f" ---|---|---")
    print(f"2 {board[2][0]} | {board[2][1]} | {board[2][2]}")
def win_check(player):
    for i in range(3):
        #horizontal cheack
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        #vertical cheack
        elif board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        #diagnal check[1]
        elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        #diagnal check[2]
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
    return False
def board_full():

    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                return False
    return True
def valid(i,j):
    if board[i][j] == " ":
        return True
    return False

def handle(user_input,user_data):
    tic_tac_toe()
    #resetting the board after the game is over
    for i in range(3):
        for j in range(3):
            board[i][j]=" "