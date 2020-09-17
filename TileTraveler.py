position = 11
travel = ""
while position != 31:
    if position == 11:
        print("You can travel: (N)orth.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "n":
            position += 1
        else:
            print("Not a valid direction!")
    elif position == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "n" or travel == "e" or travel == "s":
            if travel == "n":
                position += 1
            elif travel == "e":
                position += 10
            elif travel == "s":
                position -= 1
        else:
            print("Not a valid direction!")

    elif position == 13:
        print("You can travel: (E)ast or (S)outh.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "e" or travel == "s":
            if travel == "e":
                position += 10
            elif travel == "s":
                position -= 1
        else:
            print("Not a valid direction!")

    elif position == 21:
        print("You can travel: (N)orth.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "n":
            position += 1
        else:
            print("Not a valid direction!")

    elif position == 22:
        print("You can travel: (S)outh or (W)est.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "s" or travel == "w":
            if travel == "s":
                position -= 1
            elif travel == "w":
                position -= 10
        else:
            print("Not a valid direction!")

    elif position == 23:
        print("You can travel: (E)ast or (W)est.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "e" or travel == "w":
            if travel == "e":
                position += 10
            elif travel == "w":
                position -= 10
        else:
            print("Not a valid direction!")

    elif position == 33:
        print("You can travel: (S)outh or (W)est.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "s" or travel == "w":
            if travel == "s":
                position -= 1
            elif travel == "w":
                position -= 10

        else:
            print("Not a valid direction!")


    elif position == 32:
        print("You can travel: (N)orth or (S)outh.")
        travel = input("Direction: ")
        travel = travel.lower()
        if travel == "n" or travel == "s":
            if travel == "n":
                position += 1
            elif travel == "s":
                position -= 1

        else:
            print("Not a valid direction!")

print("Victory!")