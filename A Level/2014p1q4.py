import random
global pond
pond = [ ["." for i in range(15)] for i in range(8)]


def print_pond():
    for i in range(8):
        for j in range(15):
            print(pond[i][j],end=" ")
        print()

def fishes():
    for i in range(3):
        x = random.randint(0,14)
        y = random.randint(0,7)
        pond[y][x] = "F"

x_coord = int(input("Enter the x coordinate(1 to 15): "))
y_coord = int(input("Enter the y coordincate(1 to 8): "))

def food(x_coord,y_coord):
    if pond[y_coord - 1][x_coord - 1] == "F":
        pond[y_coord - 1][x_coord - 1] = "H"
    else:
        pond[y_coord - 1][x_coord - 1] = "P"

fishes()
food(x_coord,y_coord)
print_pond()
