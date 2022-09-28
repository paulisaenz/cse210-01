
# File 02 Ponder and Prove Assignment: Tic-Tac-Toe
# Author: Paula Sáenz

board =["1","2","3",
        "4","5","6",
        "7","8","9",]

def main():
    #Display initial board
    display_board()
    user_imput()
    pass

def game_loop():
    # while game_still_going:
    #     user_imput()
    #     check_results()
    #     flip_player()
    pass

def display_board():
    print(board[0], " | ", board[1], " | ", board[2])
    print("-  +  -  +  -")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-  +  -  +  -")
    print(board[6], " | ", board[7], " | ", board[8])
    pass

def user_imput():
    position = input("{user}'s turn to choose a square (1-9): ")
    position = int(position) - 1

    # if x = user:
    #     board[position] = "x"
    # elif o = user:
    #     board[position] = "o"
    
    display_board()
    pass

def update_board():
    pass

def check_results():
        #check for wins
            #check rows
            #check columns
            #check diagonals
        #check tie
        pass

def flip_player():
    pass


main()