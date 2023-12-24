maps = [' ', '0', '1', '2',
        '0', "-", "-", "-",
        '1', "-", "-", "-",
        '2', "-", "-", "-"]

pobeda = [[5, 6, 7],
          [9, 10, 11],
          [13, 14, 15],
          [5, 9, 13],
          [6, 10, 14],
          [7, 11, 15],
          [5, 10, 15],
          [7, 10, 13]]


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2], end=" ")
    print(maps[3])

    print(maps[4], end=" ")
    print(maps[5], end=" ")
    print(maps[6], end=" ")
    print(maps[7])

    print(maps[8], end=" ")
    print(maps[9], end=" ")
    print(maps[10], end=" ")
    print(maps[11])

    print(maps[12], end=" ")
    print(maps[13], end=" ")
    print(maps[14], end=" ")
    print(maps[15])


def get_map_index(player_input):
    mapping = {
        1: 5, 2: 6, 3: 7,
        4: 9, 5: 10, 6: 11,
        7: 13, 8: 14, 9: 15
    }
    return mapping.get(player_input)


def step_maps(step, symbol):
    ind = get_map_index(step)
    if ind is None or maps[ind] != "-":
        print('Недопустимый ход, пропуск хода.')
    else:
        maps[ind] = symbol


def get_result():
    win = ""

    for i in pobeda:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win

game_over = False
player1 = True

while game_over == False:
    print_maps()
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not player1

print_maps()
print("Победил", win)
