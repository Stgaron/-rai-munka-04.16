from random import randint
print("Üdvözöllek a 21 es játékba")
print("A cél az,hogy a szám legyen minnél közelebb a 21-hez,aki túllépi az veszt azonnal")
print("Ebben a játékban a lapok száma 1 és 10 között lesz")
print("3 kártyád van")
print("A kártyáidból el is tudsz tüntetni")
def jatek_ember():
    if jatekmod == "ember":
        print("Akkor Ember ellen szeretnél játszani")
        print("Az első játékos:")
        kartyak1 = [randint(1, 10) for _ in range(3)]
        print(f"A kártyáid száma = {kartyak1}")
        print(f"A kártyáid összege = {sum(kartyak1)}")
        kivonas = int(input("Ha szeretnél eltüntetni egy kártyát írd be a számát, ha semmit akkor 4-et: "))
        if kivonas in [1, 2, 3]:
            vegsoszam = sum(kartyak1) - kartyak1[kivonas - 1]
        elif kivonas == 4:
            vegsoszam = sum(kartyak1)
        else:
            while kivonas < 1 or kivonas > 4:
                print("Ide mást mint (1,2,3,4)")
                kivonas = int(input("Ha szeretnél eltüntetni egy kártyát írd be a számát, ha semmit akkor 4-et: "))
            vegsoszam = sum(kartyak1)
        print(f"A végső számod = {vegsoszam}")
        print("A második játékos:")
        kartyak2 = [randint(1, 10) for j in range(3)]
        print(f"A kártyáid száma = {kartyak2}")
        print(f"A kártyáid összege = {sum(kartyak2)}")
        kivonas = int(input("Ha szeretnél eltüntetni egy kártyát, írd be a számát, ha nem akkor írd azt, hogy 4: "))
        if kivonas in [1, 2, 3]:
            masodikvegsoszam = sum(kartyak2) - kartyak2[kivonas - 1]
        elif kivonas == 4:
            masodikvegsoszam = sum(kartyak2)
        else:
            while kivonas < 1 or kivonas > 4:
                print("Ide mást írtál mint  (1,2,3,4)")
                kivonas = int(input("Ha szeretnél eltüntetni egy kártyát, írd be a számát, ha nem akkor írd azt, hogy 4: "))
            masodikvegsoszam = sum(kartyak2)
        print(f"A végső számod = {masodikvegsoszam}")
        if vegsoszam > 21 and masodikvegsoszam > 21:
            print("Mindkét játékos túllépte a 21-et, döntetlen!")
        elif vegsoszam > 21:
            print("Az első játékos túllépte a 21-et, ezért a második játékos nyer!")
        elif masodikvegsoszam > 21:
            print("A második játékos túllépte a 21-et, ezért az első játékos nyer!")
        elif vegsoszam > masodikvegsoszam:
            print("Az első játékos nyert")
        elif masodikvegsoszam > vegsoszam:
            print("A második játékos nyert")
        else:
            print("Döntetlen")

def robot():
    if jatekmod =="robot":
        print("idk")
jatek = 'i'
while jatek == 'i':
    jatekmod = input("Kérem válasszon játékmódot (ember,robot): ")
    if jatekmod == "ember":
        jatek_ember()
    elif jatekmod == "robot":
        robot()
    else:
        print("Nem értelmezhető játékmód!")

    if jatekmod in ("ember", "robot"):
        vegekerdes = ""
        while vegekerdes not in ('i', 'n'):
            vegekerdes = input("Szeretne új játékot játszani? (i/n): ")
            if vegekerdes not in ('i', 'n'):
                print("Nem értelmezhető válasz! Csak i és n lehet!")
            else:
                jatek = vegekerdes