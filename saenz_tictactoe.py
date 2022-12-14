# board = ["1","2","3","4","5","6","7","8","9"]

spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}


def main():
    playing = True
    complete = False
    turn = 0
    prev_turn = -1

    
    while playing:
        display_board()

        if prev_turn == turn:
            print("Sorry, this spot is invalid. Please pick another one! ")
        prev_turn = turn

        player_turn = str((turn % 2) + 1)

        print()

        print(f"It's player's {player_turn} turn! Pick your spot or press q to quit. ")

        print()
        position = input("Choose a position (1-9): ")

        if position == "q":
            playing = False
        elif str(position) and int(position) in spots:
            if not spots[int(position)] in {"x", "o"}:
                turn +=1
                spots[int(position)] = player(turn)

        # Check if someone won the game
        if check_for_wins(spots):
            playing = False
            complete = True

        # Check if there was a tie
        if turn > 8:
            playing = False
    
    display_board()

    if complete:
        if player(turn) == "x":
            print("")
            print("Congratulations! Player 1 won!")
        else:
            print("")
            print("Congratulations! Player 2 won!")
    
    else:
        print("")
        print ("It was a tie!")
        
    print("")
    print("Thanks for playing!")
    
    

def display_board():
    print()
    print(f"{spots[1]}  |  {spots[2]} |  {spots[3]}")
    print("-  +  -  +  -")
    print(f"{spots[4]}  |  {spots[5]} |  {spots[6]}")
    print("-  +  -  +  -")
    print(f"{spots[7]}  |  {spots[8]} |  {spots[9]}")

def player(turn):
    if turn %2 == 0:
        return "o"
    else:
        return "x"

def check_for_wins(spots):

    # Check row winner
    if (spots[1] == spots[2] == spots[3]) or (spots[4] == spots[5] == spots[6]) or (spots[7] == spots[8] == spots[9]):
        return True

    # Check column winner
    elif (spots[1] == spots[4] == spots[7]) or (spots[2] == spots[5] == spots[8]) or (spots[3] == spots[6] == spots[9]):
        return True
    
    # Check diagonal winner
    elif (spots[1] == spots[5] == spots[9]) or (spots[3] == spots[5] == spots[7]):
        return True
    
    else:
        return False


if __name__ == "__main__":
    main()