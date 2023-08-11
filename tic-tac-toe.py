print("""Правила игры:
    1. В игре принимают участие два игрока: "Игрок (х)" и "Игрок (o)". 
    2. Игроки ходят по очереди. Первый ход всегда делает Игрок (х).
    3. Игроки вводят в игровое поле координаты в виде двузначных чисел: 
        • первая цифра — горизонтальная координата; 
        • вторая цифра — вертикальная координата.
       Координаты вводятся в диапазоне от 1 до 3 последовательно, без пробелов.
    4. Если введенная координата меньше 1 или больше 3, то ей присваивается значение 1 или 3 соответственно.
    5. Если ячейка, которую задает игрок занята, необходимо повторно ввести координаты свободной ячейки игрового поля.
    6. Побеждает игрок, который первым полностью заполнит линию игрового поля тремя значениями 'x' или 'o' 
    (по горизонтали, вертикали или диагонали). В противном случае победитель отсутствует и объявляется ничья.""")

# Игровое поле
my_playboard = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
# Условие победы Игрока (х)
x_win_condition = False
# Условие победы Игрока (о)
o_win_condition = False
# Условие отсутствия победителя (Ничья)
draw_condition = False


# Печать игрового поля
def playboard():
    print("\n———————————————")
    for i in range(4):
        for j in range(4):
            print(my_playboard[i][j], end=" ")
        print()
    print("———————————————")


# Ввод координат
def coord_input(coord):
    # Проверка диапазона координат
    if int(coord[0]) <= 1:
        coord_i = 1
    elif int(coord[0]) >= 3:
        coord_i = 3
    else:
        coord_i = int(coord[0])
    if int(coord[1]) <= 1:
        coord_j = 1
    elif int(coord[1]) >= 3:
        coord_j = 3
    else:
        coord_j = int(coord[1])
    return [coord_i, coord_j]


# Проверка условий победы
def winner_check(player):
    if my_playboard[1].count(player) == 3 \
            or my_playboard[2].count(player) == 3 \
            or my_playboard[3].count(player) == 3 \
            or my_playboard[1][1] == player and my_playboard[2][2] == player and my_playboard[3][3] == player \
            or my_playboard[1][3] == player and my_playboard[2][2] == player and my_playboard[3][1] == player \
            or my_playboard[1][1] == player and my_playboard[2][1] == player and my_playboard[3][1] == player \
            or my_playboard[1][2] == player and my_playboard[2][2] == player and my_playboard[3][2] == player \
            or my_playboard[1][3] == player and my_playboard[2][3] == player and my_playboard[3][3] == player:
        return True
    else:
        return False


#  Проверка условия отсутствия победителя (Ничья)
def draw_check():
    if " " in my_playboard[1] or " " in my_playboard[2] or " " in my_playboard[3]:
        return False
    else:
        return True


# Печать начального игрового поля
playboard()
# Цикл проверки победителя
while x_win_condition == False and o_win_condition == False and draw_condition == False:
    x_coord = input("Игрок (x), ваш ход: ")  # Ввод координат Игроком (x)
    # Ячейка занята. Повторный ввод Игроком (x)
    while my_playboard[coord_input(x_coord)[0]][coord_input(x_coord)[1]] != " ":
        x_coord = input("Игрок (x), ячейка занята, введите координаты свободной ячейки: ")
    # Замена значения пустой ячейки на 'х'
    my_playboard[coord_input(x_coord)[0]][coord_input(x_coord)[1]] = "x"
    # Ввод координат Игроком (о)
    o_coord = input("Игрок (o), ваш ход: ")
    # Ячейка занята. Повторный ввод Игроком (о)
    while my_playboard[coord_input(o_coord)[0]][coord_input(o_coord)[1]] != " ":
        o_coord = input("Игрок (o), ячейка занята, введите координаты свободной ячейки: ")
    # Замена значения пустой ячейки на 'о'
    my_playboard[coord_input(o_coord)[0]][coord_input(o_coord)[1]] = "o"
    playboard()
    # Проверка условия победы Игрока (х)
    x_win_condition = winner_check("x")
    # Проверка условия победы Игрока (о)
    o_win_condition = winner_check("o")
    draw_condition = draw_check()
# Проверка условия победы Игрока (х) по праву первого хода.
if x_win_condition:
    print("Победил Игрок (х)!")
elif o_win_condition:
    print("Победил Игрок (о)!")
else:
    print("Ничья.")
