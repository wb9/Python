def koszulki():
    zadruk = float(input("Nadruk z jednej(1) strony czy z dwóch?(2) "))
    koszulka = float(input("Koszulka nasza(1) czy klienta?(2) "))
    kolory = float(input("Podaj ilość kolorów: "))

    cena = 0

    if zadruk == 1:
        cena += 30
    elif zadruk == 2:
        cena += 50

    if koszulka == 1:
        cena += 25
    else:
        pass

    print(cena)