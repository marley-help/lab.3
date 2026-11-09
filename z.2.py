liczby = []
liczba = 2

while len(liczby) < 10:
    dzielnik = 2

    while dzielnik < liczba:
        if liczba % dzielnik == 0:
            break
        dzielnik += 1

        if dzielnik == liczba:
            liczby.append(liczba)
        liczba += 1
    print("," .join(map((str, liczby))))

