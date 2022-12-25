"""
Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:

 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9

"""
import emoji

print(emoji.emojize('Python is :thumbs_up:'))

# Выводим карту на экран
def Print_Maps():
    print(maps[0], end="   ")
    print(maps[1], end="   ")
    print(maps[2])

    print(maps[3], end="   ")
    print(maps[4], end="   ")
    print(maps[5])

    print(maps[6], end="   ")
    print(maps[7], end="   ")
    print(maps[8])


# Делаем ход в ячейку
def Step_Maps(step, symbol):
    index = maps.index(step)
    maps[index] = symbol


# Получить текущий результат игры
def Get_Result():
    win = ""

    for i in victory:
        if maps[i[0]] == emoji.emojize(":plus:") and maps[i[1]] == emoji.emojize(":plus:") and maps[i[2]] == emoji.emojize(":plus:"):
            win = emoji.emojize(":plus:")
        if maps[i[0]] == emoji.emojize(":nazar_amulet:") and maps[i[1]] == emoji.emojize(":nazar_amulet:") and maps[i[2]] == emoji.emojize(":nazar_amulet:"):
            win = emoji.emojize(":nazar_amulet:")

    return win


# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


# Основная программа
game_over = False
player1 = True

count = 9
while game_over == False and count != 0:

    #Печать карты
    Print_Maps()

    #Приглашение к вводу символа в ячейку
    if player1 == True:
        symbol = emoji.emojize(":plus:")
        step = int(input("Ход Игрока 1: "))
        count -= 1
    else:
        symbol = emoji.emojize(":nazar_amulet:")
        step = int(input("Ход Игрока 2: "))
        count -= 1

    Step_Maps(step, symbol)  # ход в указанную ячейку
    winner = Get_Result()  # определение победителя
    
    if winner != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)


# Игра окончена. Покажем карту. Объявим победителя.
Print_Maps()

if count != 0:
    print(emoji.emojize(f":clapping_hands: :clapping_hands: :clapping_hands: Победил, {winner} - :1st_place_medal:"))
else:
    print('Игра завершилась ничьей')
