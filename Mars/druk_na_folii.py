def druk_na_folii():
    import math
    szerokosc = float(input("Podaj szerokość w cm: "))
    wysokosc = float(input("Podaj wysokość w cm: "))
    wymiar = szerokosc*wysokosc/10000

    print("")
    print("Wymiar wydruku to " + str(wymiar) + "m².")

    wymiar = math.ceil(wymiar)
    cena = wymiar*50

    print("Koszt to " + str(cena) + "zł + 23% VAT.")