def koszulki():
    zadruk = float(input("Nadruk z jednej(1) strony czy z dwóch?(2) "))
    koszulka = float(input("Koszulka nasza(1) czy klienta?(2) "))
    kolory = float(input("Podaj ilość kolorów: "))
    wymiar = float(input("Jaki wymiar ma folia na koszulkę? [1] - do A4 | [2] - większy niż A4 "))

    cena = 0

    if zadruk == 1:
        cena += 30
    elif zadruk == 2:
        cena += 45

    if koszulka == 1:
        cena += 20
    else:
        pass

    if kolory > 1:
        cena = cena+(kolory*10)
    else:
        pass

    if wymiar == 2:
        cena *= 1.3
    else:
        pass

    print(cena)