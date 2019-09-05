import baner
import tabliczka_folia_PCV
import koszulki

print ("Wybór: ")
print("[1] BANERY")
print("[2] TABLICZKA PCV + FOLIA")
print("[3] KOSZULKI")
print("[4]")
print("[5]")

numer = float(input("Podaj numer: "))

if numer == 1:
    baner.baner()
elif numer == 2:
    tabliczka_folia_PCV.tabliczka()
elif numer == 3:
    koszulki.koszulki()