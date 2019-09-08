def tabliczki_grawerowane():
    szerokosc = float (input ("Podaj szerokość tabliczki w cm: "))
    wysokosc = float (input ("Podaj wysokość tabliczki w cm: "))

    wymiar = szerokosc*wysokosc
    cena = 0

    if wymiar <= 40:
      print("Tabliczka ma wymiar " + str(wymiar) + "cm². Koszt to 20 zł + 23% VAT.")
    elif 40 < wymiar < 200:
      cena = wymiar*0.3
      print("Tabliczka ma wymiar " + str(wymiar) + "cm². Koszt to " + str(cena) + "zł + 23% VAT.")
    elif 200 < wymiar:
      cena = wymiar*0.25
      print("Tabliczka ma wymiar " + str(wymiar) + "cm². Koszt to " + str(cena) + "zł + 23% VAT.")