# Процедурная парадигма, т.к. нам нужен вывод и возвращать ничего не нужно


def table_mult(n):

    for i in range(1, n + 1):
        x = ""
        for j in range(1, n + 1):
            x = x + f"  {i}*{j}={i * j}"
        print(x+'\n')

n = int(input("Введите число n: "))
table_mult(n)
