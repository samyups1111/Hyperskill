t = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def screen():
    print("--------")
    print(f"| {t[0]} {t[1]} {t[2]} |")
    print(f"| {t[3]} {t[4]} {t[5]} |")
    print(f"| {t[6]} {t[7]} {t[8]} |")
    print("--------")
screen()
def update_board():
    global row1, row2, row3, column1, column2, column3, diagonal1, diagonal2, possibilities
    row1 = f"{t[0]}{t[1]}{t[2]}"
    row2 = f"{t[3]}{t[4]}{t[5]}"
    row3 = f"{t[6]}{t[7]}{t[8]}"
    column1 = f"{t[0]}{t[3]}{t[6]}"
    column2 = f"{t[1]}{t[4]}{t[7]}"
    column3 = f"{t[2]}{t[5]}{t[8]}"
    diagonal1 = f"{t[0]}{t[4]}{t[8]}"
    diagonal2 = f"{t[2]}{t[4]}{t[6]}"
    possibilities = [row1, row2, row3, column1, column2,
    column3, diagonal1, diagonal2]
def results():
    if "XXX" in possibilities:
        print("X wins")
        return True
    elif "OOO" in possibilities:
        print("O wins")
        return True
    elif " " not in t:
        if ("XXX" not in t) and ("OOO" not in t):
            print("Draw")
            return True
    else:
        return False
def plug_coordinate(coordinate):
    global t
    if coordinate == "1 1":
        if t[6] == " ":
            t[6] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "1 2":
        if t[3] == " ":
            t[3] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "1 3":
        if t[0] == " ":
            t[0] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 1":
        if t[7] == " ":
            t[7] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 2":
        if t[4] == " ":
            t[4] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "2 3":
        if t[1] == " ":
            t[1] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 1":
        if t[8] == " ":
            t[8] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 2":
        if t[5] == " ":
            t[5] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    elif coordinate == "3 3":
        if t[2] == " ":
            t[2] = "O" if t.count("X") > t.count("O") else "X"
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
options = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]
def check_coordinate(coordinate):
    if coordinate not in options:
        print("Coordinates should be from 1 to 3!")
        return False
    elif coordinate[0] and coordinate[2] not in "1234567890":
        print("You should enter numbers!")
        return False
    else:
        return True
while " " in t:
    coordinate = input("Enter the coordinates: ")
    if check_coordinate(coordinate) == False:
        continue
    else:
        update_board()
        if plug_coordinate(coordinate) == False:
            continue
        else:
            update_board()
            screen()
            if results() == True:
                break
