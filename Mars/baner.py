def baner():
    dlugosc_banera = float (input ("Podaj długośc banera w metrach: "))
    wysokosc_banera = float (input ("Podaj wysokość banera w metrach: "))
    calkowity_wymiar_banera = wysokosc_banera*dlugosc_banera

    cena = 0

    if calkowity_wymiar_banera <= 5:
        cena = calkowity_wymiar_banera*50
    elif 10 > calkowity_wymiar_banera > 5:
        cena = calkowity_wymiar_banera*45
    elif 10 < calkowity_wymiar_banera:
        cena = calkowity_wymiar_banera*40

    print("")

    print("Powierzchnia banera to " + str(calkowity_wymiar_banera) + "m². Całkowity koszt to " + str(cena) + "zł + 23% VAT.")