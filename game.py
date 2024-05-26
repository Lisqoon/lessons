onename = input("Как зовут первого игрока?")
print(onename)
twoname = input("Как зовут второго игрока?")
print(twoname)
print(onename, "и",  twoname, "вы можете приступать к игре!")

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
        if maps == 9:
            print("Ничья")
        break

    return win

game_over = False
player1 = True

while game_over == False:
    print_maps()

    if player1 == True:
        print(onename+",",  "ваш ход крестиком: ")
        symbol = "X"
        step = int(input())
    else:
        print(twoname+",", "ваш ход ноликом: ")
        symbol = "O"
        step = int(input())

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()
print("Победили", win)