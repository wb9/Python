import baner
import tabliczka_folia_PCV
import koszulki
import druk_na_folii
import UV_PCV
import tabliczki_grawerowane
import folia_ploter

def main():

    print ("Wybór: ")
    print("[1] BANERY")
    print("[2] KOSZULKI")
    print("[3] TABLICZKA PCV + FOLIA")
    print("[4] DRUK NA FOLII")
    print("[5] DRUK UV NA PCV")
    print("[6] TABLICZKI GRAWEROWANE")
    print("[7] FOLIA PLOTER")
    print("")
    numer = float(input("Podaj numer: "))
    print("")
    if numer == 1:
        baner.baner()
    elif numer == 2:
        koszulki.koszulki()
    elif numer == 3:
        tabliczka_folia_PCV.tabliczka()
    elif numer == 4:
        druk_na_folii.druk_na_folii()
    elif numer == 5:
        UV_PCV.uv_pcv()
    elif numer == 6:
        tabliczki_grawerowane.tabliczki_grawerowane()
    elif numer == 7:
        folia_ploter.folia_ploter()

    print("")
    koniec = input("Zacząć od nowa? T/N  ").lower()
    if koniec == "t":
        main()
    else:
        exit()

main()