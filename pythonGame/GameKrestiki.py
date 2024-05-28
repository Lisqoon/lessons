onename = input("Как зовут первого игрока?")
twoname = input("Как зовут второго игрока?")
print("*****************************************")
print("***************КАК ИГРАТЬ?***************")
print("Ходить в игре нужно вводя координаты x и y!")
print("Сначала вводится номер строки, затем через пробел номер стобца!")
print("*****************************************")
print(onename, "и", twoname, "вы можете приступать к игре!")


def pole():
    print(f"* 0 1 2")
    print(f"0|{field[0][0]}|{field[0][1]}|{field[0][2]}|")
    print(f"1|{field[1][0]}|{field[1][1]}|{field[1][2]}|")
    print(f"2|{field[2][0]}|{field[2][1]}|{field[2][2]}|")


def spros():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Ввод координат делаеся числами, а не буквами! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона, попробуйте ещё раз! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win(): #
    victories = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in victories:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    pole()
    if count % 2 == 1:
        print(onename + "", "ходит крестиком!")
    else:
        print(twoname + "", "ходит ноликом!")

    x, y = spros()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Победила дружба!")
        break