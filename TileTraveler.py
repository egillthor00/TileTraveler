position = 11

while position != 31:
    if position == 11:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")
    elif travel == "n":
            position += 1
        else:
            print("Not a valid direction!")
    elif position == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        travel = input.lower("Direction")
        elif travel == "n" or travel == "e" or travel == "s":
            elif travel == "n":
                position +=1

        else:
            print("not a valid direction!")

    elif position == 13:
        print("You can travel: (E)ast or (S)outh.")
        travel = input.lower("Direction")
        elif  travel == "e" or travel == "s":
            elif travel == "n":
                position +=1  

    elif position == 21:
        print("You can travel: (E)ast or (W)est.")
        travel = input.lower("Direction")

    elif position == 22:
        print("You can travel: (S)outh or (W)est.")
        travel = input.lower("Direction")

    elif position == 23:
        print("You can travel: (N)orth or (S)outh.")
        travel = input.lower("Direction")

    elif position == 33:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    elif position == 32:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")


print("Victory!")