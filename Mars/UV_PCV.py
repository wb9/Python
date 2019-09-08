def uv_pcv():
     import math

     dlugosc = float (input("Podaj długość w centymetrach: "))
     szerokosc = float (input("Podaj szerokość w centymetrach: "))

     powierzchnia = (dlugosc*szerokosc)/10000
     print("")
     print("Powierzchnia to " + str(powierzchnia) + "m².")
     powierzchnia = float (math.ceil(powierzchnia))
     print("Powierzchnia po zaokrągleniu w górę to " + str(powierzchnia) + "m².")
     cena = powierzchnia*150
     print("Koszt to " + str(cena) + "zł + 23% VAT.")