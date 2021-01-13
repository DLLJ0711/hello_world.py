squareSize = int(input('How big is the square: '))
i = 0


while(i < squareSize):
    j = 0
    while(j < squareSize):
        j += 1
        print("*", end = " ")
    i += 1
    print()