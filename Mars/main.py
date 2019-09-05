import baner
import tabliczka_folia_PCV
import koszulki
#import druk_na_folii
#import UV_PCV

def main():

    print ("Wybór: ")
    print("[1] BANERY")
    print("[2] TABLICZKA PCV + FOLIA")
    print("[3] KOSZULKI")
    print("[4] DRUK NA FOLII")
    print("[5] DRUK UV NA PCV")

    numer = float(input("Podaj numer: "))

    if numer == 1:
        baner.baner()
    elif numer == 2:
        tabliczka_folia_PCV.tabliczka()
    elif numer == 3:
        koszulki.koszulki()
    #elif numer == 4:
    #    druk_na_folii.druk_na_folii()
    #elif numer == 5:
    #    UV_PCV.uv_pcv()

    koniec = input("Zacząć od nowa? T/N  ").lower()
    if koniec == "t":
        main()
    else:
        exit()

main()