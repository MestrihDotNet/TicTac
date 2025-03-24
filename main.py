# declaring the 2d matrix
ttt = [[" "," "," "],[" "," "," "],[" "," "," "]]

winner = False

def showgame():
    for row in ttt:
        print(" | ".join(row))
        print("-" * 9)


def checkwinner():
    # Check rows
    for row in ttt:
        if row[0] == row[1] == row[2] and row[0] != " ":
            print(f"Player {row[0]} wins horizontally!")
            return True

    # Check columns
    for col in range(3):
        if ttt[0][col] == ttt[1][col] == ttt[2][col] and ttt[0][col] != " ":
            print(f"Player {ttt[0][col]} wins vertically!")
            return True

    # Check diagonals
    if ttt[0][0] == ttt[1][1] == ttt[2][2] and ttt[0][0] != " ":
        print(f"Player {ttt[0][0]} wins diagonally (top-left to bottom-right)!")
        return True
    elif ttt[2][0] == ttt[1][1] == ttt[0][2] and ttt[2][0] != " ":
        print(f"Player {ttt[2][0]} wins diagonally (top-right to bottom-left)!")
        return True

    return False  # Return False if no winner found

def checkdraw():
    for row in ttt:
        if " " in row:
            return False
    print("it's a draw")
    return True


print("welcome to tic-tac-toe!")
player1Row = int(input("you are player one you will have the 'X', please choose which row do you want to start with? \n (1) __|__|__ \n (2) __|__|__ \n (3) __|__|__ \n Row: "))
player1Column = int(input("now choose which Column you wanna change (1)|(2)|(3): "))
ttt[player1Row-1][player1Column-1] = 'X'
showgame()

player2Row = int(input("player 2 choose a row: "))
player2Column = int(input("player 2 choose a column: "))
ttt[player2Row-1][player2Column-1]= "O"
showgame()


while winner == False:
    if checkdraw():
        break
    else:
        if checkwinner():
            break
        else:
            player1Row = int(input("Player 1 Row: "))
            player1Column = int(input("Player 1 Column: "))
            if ttt[player1Row - 1][player1Column - 1] == " ":
                ttt[player1Row - 1][player1Column - 1] = 'X'
            else:
                print("Invalid, try again!!")
                player1Row = int(input("Player 1 Row: "))
                player1Column = int(input("Player 1 Column: "))
                if ttt[player1Row - 1][player1Column - 1] == " ":
                    ttt[player1Row - 1][player1Column - 1] = 'X'
            showgame()
    if checkdraw():
        break
    else:
        if checkwinner():
            break
        else:
            player2Row = int(input("Player 2 Row: "))
            player2Column = int(input("Player 2 Column: "))
            if ttt[player2Row - 1][player2Column - 1] == " ":
                ttt[player2Row - 1][player2Column - 1] = 'O'
            else:
                print("Invalid, try again!!")
                player2Row = int(input("Player 2 Row: "))
                player2Column = int(input("Player 2 Column: "))
                if ttt[player2Row - 1][player2Column - 1] == " ":
                    ttt[player2Row - 1][player2Column - 1] = 'O'
            showgame()



