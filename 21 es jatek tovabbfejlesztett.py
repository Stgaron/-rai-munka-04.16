from random import randint
print("Üdvözöllek a 21 es játékba")
print("A cél az,hogy a szám legyen minnél közelebb a 21-hez,aki túllépi az veszt azonnal")
print("Ebben a játékban a lapok száma 2 és 11 között lesz")
print("2 kártyád van")
print("A kártyáidból el is tudsz tüntetni")
def jatek_ember():
    if jatekmod == "e":
        print("Akkor Ember ellen szeretnél játszani")
        print("Az első játékos:")
        kartyak1 = [randint(2, 11) for _ in range(2)]
        print(f"A kártyáid száma = {kartyak1}")
        print(f"A kártyáid összege = {sum(kartyak1)}")
        if sum(kartyak1) > 16:
            ujrakero=input("Szeretnél húzni még egy kártyát?,(i,n):")
            if ujrakero=="i":
                kartyak1.append(randint(2, 11))
                sum(kartyak1)
                print(kartyak1)
            else:
                print("")

        vegsoszam = sum(kartyak1)
        print(f"A végső számod = {vegsoszam}")
        print("A második játékos:")
        kartyak2 = [randint(2, 11) for j in range(2)]
        print(f"A kártyáid száma = {kartyak2}")
        print(f"A kártyáid összege = {sum(kartyak2)}")
        if sum(kartyak2) > 16:
            ujrakero=input("Szeretnél húzni még egy kártyát?,(i,n):")
            if ujrakero=="i":
                kartyak1.append(randint(2, 11))
                sum(kartyak2)
                print(f"A kártyáid száma = {kartyak2}")
            else:
                print("")

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
    if jatekmod =="r":
        print("idk")
jatek = 'i'
while jatek == 'i':
    jatekmod = input("Kérem válasszon játékmódot ember vagy robot(e,r): ")
    if jatekmod == "e":
        jatek_ember()
    elif jatekmod == "r":
        robot()
    else:
        print("Nem értelmezhető játékmód!")

    if jatekmod in ("e", "r"):
        vegekerdes = ""
        while vegekerdes not in ('i', 'n'):
            vegekerdes = input("Szeretne új játékot játszani? (i/n): ")
            if vegekerdes not in ('i', 'n'):
                print("Nem értelmezhető válasz! Csak i és n lehet!")
            else:
                jatek = vegekerdes