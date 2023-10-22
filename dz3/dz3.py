import random

field = ['1', "|", '2', "|", '3',
         "-", "-", "-", "-", "-",
         '4', "|", '5', "|", '6',
         "-", "-", "-", "-", "-",
         '7', "|", '8', "|", '9']


def print_field(field):
    x = ''
    for i in range(len(field)):
        if i % 5 == 0:
            print(x)
            x = ''
        x = x + str(field[i])
        if i == len(field) - 1:
            print(x)


def game(player, comp, f):
    while True:
        if f[0] == f[2] == f[4] == 'X' or f[10] == f[12] == f[14] == 'X' or f[20] == f[22] == f[24] == 'X' \
                or f[0] == f[10] == f[20] == 'X' or f[2] == f[12] == f[22] == 'X' or f[4] == f[14] == f[24] == 'X' \
                or f[0] == f[12] == f[24] == 'X' or f[4] == f[12] == f[20] == 'X':
            print("Победили крестики!")
            break
        if f[0] == f[2] == f[4] == '0' or f[10] == f[12] == f[14] == '0' or f[20] == f[22] == f[24] == '0' \
                or f[0] == f[10] == f[20] == '0' or f[2] == f[12] == f[22] == '0' or f[4] == f[14] == f[24] == '0' \
                or f[0] == f[12] == f[24] == '0' or f[4] == f[12] == f[20] == '0':
            print("Победили нолики!")
            break
        print_field(f)
        hod = int(input(f"Введите номер ячейки в которой хотите поставить {player}: "))
        prov = {1: 0,
                2: 2,
                3: 4,
                4: 10,
                5: 12,
                6: 14,
                7: 20,
                8: 22,
                9: 24}

        if f[prov[hod]] == "X" or f[prov[hod]] == "0":
            print("Ячейка занята, выберите другую")
            continue
        else:
            f[prov[hod]] = player

        while True:
            hod_comp = random.randint(1, 9)
            if f[prov[hod_comp]] == "X" or f[prov[hod]] == "0":
                continue
            else:
                f[prov[hod_comp]] = comp
                break


def start_game(field):
    s = input("Выберите кем играть X или 0: ")
    if s == "x" or s == "X" or s == "х" or s == "Х":
        print("Вы выбрали Х ходите первым, компьютер играет 0")
        s = "X"
        c = "0"

    if s == "0":
        print("Вы выбрали 0, компьютер ходит первым, компьютер играет Х")
        s = "0"
        c = "X"
    game(s, c, field)


start_game(field)
