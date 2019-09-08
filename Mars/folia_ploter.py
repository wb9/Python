def folia_ploter():

    dlugosc_folii = float(input("Podaj długość folii w cm: "))
    dlugosc_linii_ciecia = float(input("Podaj długość linii cięcia w m: "))
    folia_transportowa = float(input("Folia transportowa? Tak(1)/Nie(2) ").lower())

    if folia_transportowa == 1:
        folia_transportowa = dlugosc_linii_ciecia*dlugosc_folii*0.2
    else:
        pass

    cena = (dlugosc_folii*0.15)+(dlugosc_linii_ciecia*3)+folia_transportowa

    if cena < 20:
        print("Cena za cięcie to 20 zł + 23% VAT.")
    else:
        print("Cena za cięcie to " + str(cena) + "zł + 23% VAT.")