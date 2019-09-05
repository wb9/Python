def baner():
    dlugosc_banera = float (input ("Podaj długośc banera w metrach: "))
    wysokosc_banera = float (input ("Podaj wysokość banera w metrach: "))
    calkowity_wymiar_banera = wysokosc_banera*dlugosc_banera

    if calkowity_wymiar_banera <= 5:
        print(calkowity_wymiar_banera*50)
    elif 10 > calkowity_wymiar_banera > 5:
        print(calkowity_wymiar_banera*45)
    elif 10 < calkowity_wymiar_banera:
        print(calkowity_wymiar_banera*40)