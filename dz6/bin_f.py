mass = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
chislo = 0
i = len(mass)//2

while True:
    if chislo in mass:
        if mass[i] == chislo:
            print(i)
            break
        elif mass[i] > chislo:
            i = i - i//2
        elif mass[i] < chislo:
            i = i + i//2
    else:
        print(-1)
        break