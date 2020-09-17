position = 11

while position != 31:
    if position == 11:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")
        if travel == "n":
            position += 1
        else:
            print("Not a valid direction!")
    if position == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        travel = input.lower("Direction")
        if travel == "n" or travel == "e" or travel == "s":
            if travel == "n":
                position +=1

        else:
            print("not a valid direction!")

    if position == 13:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    if position == 21:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    if position == 22:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    if position == 23:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    if position == 33:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")

    if position == 32:
        print("You can travel: (N)orth.")
        travel = input.lower("Direction")


print("Victory!")