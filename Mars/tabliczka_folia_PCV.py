def tabliczka():
    szerokosc_tabliczki = float (input ("Podaj szerokość tabliczki w centymetrach: "))
    wysokosc_tabliczki = float (input ("Podaj wysokość tabliczki w centymetrach: "))
    dlugosc_linii_ciecia = float (input ("Podaj długość linii cięcia w centymetrach: "))
    ilosc_kolorow = int (input ("Podaj ilość kolorów: "))
    skomplikowanie = int (input ("Podaj poziom skomplikowania 1/2/3: "))
    wymiar_tabliczki = szerokosc_tabliczki*wysokosc_tabliczki
    cena_za_wymiar = wymiar_tabliczki * 0.03
    cena_stala = 10
    cena_za_ciece = dlugosc_linii_ciecia * 0.08
    cena_za_ilosc_kolorow = 0

    if ilosc_kolorow>=2:
        cena_za_ilosc_kolorow = ilosc_kolorow * 10 / 2
    else:
        pass

    skomplikowanie_koszt = skomplikowanie / 10 + 1

    cena_koncowa = float ((cena_za_wymiar + cena_stala + cena_za_ciece + cena_za_ilosc_kolorow) * skomplikowanie_koszt)
    print("")
    print ("Cena za wymiar tabliczki " + str(cena_za_wymiar) + "zł, koszt za cięcie " +	str(cena_za_ciece) +
    "zł. Stały koszt za jeden kolor to 10 zł. Mnożnik kosztu za poziom skomplikowania to " + str(skomplikowanie_koszt) + ". Stały koszt za rozpoczęcie pracy to 10 zł.")

    print("Wymiar całej tabliczki to " + str(wymiar_tabliczki) + " cm².")
    print("Koszt wykonania to " + str(round (cena_koncowa, 2)) + "zł netto.")