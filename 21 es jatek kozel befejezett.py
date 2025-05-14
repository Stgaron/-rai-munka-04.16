from random import randint
print("Üdvözöllek a 21 es játékba")
print("A cél az,hogy a szám legyen minnél közelebb a 21-hez,aki túllépi az veszt azonnal")
print("Ebben a játékban a lapok száma 2 és 11 között lesz")
def jatek_ember():
    if jatekmod == "e":
        print("Az első játékos:")
        kartyak1 = [randint(2, 11) for _ in range(2)]
        while sum(kartyak1) >0 and sum(kartyak1) <=16:
            kartyak1.append(randint(2, 11))
        print(f"A kártyáid száma = {kartyak1}")
        print(f"A kártyáid összege = {sum(kartyak1)}")
        if sum(kartyak1) > 16 and sum(kartyak1) < 20:
            ujrakero=input("Szeretnél húzni még egy kártyát?,(i,n):")
            if ujrakero=="i":
                kartyak1.append(randint(2, 11))
                sum(kartyak1)
                print(kartyak1)
            else:
                print("")
        db=len(kartyak1)
        vegsoszam = sum(kartyak1)
        print(f"A végső számod = {vegsoszam}")
        print(f"A kártyáid darabszáma= {db}")
        print("________")
        print("A második játékos:")
        kartyak2 = [randint(2, 11) for _ in range(2)]
        while sum(kartyak2) >0 and sum(kartyak2) <=16:
            kartyak2.append(randint(2, 11))
        print(f"A kártyáid száma = {kartyak2}")
        print(f"A kártyáid összege = {sum(kartyak2)}")
        if sum(kartyak2) > 16 and sum(kartyak2)<20:
            ujrakero=input("Szeretnél húzni még egy kártyát?,(i,n):")
            if ujrakero=="i":
                kartyak2.append(randint(2, 11))
                sum(kartyak2)
                print(f"A kártyáid száma = {kartyak2}")
            else:
                print("")

        db2 = len(kartyak2)
        masodikvegsoszam = sum(kartyak2)
        print(f"A végső számod = {masodikvegsoszam}")
        print(f"A kártyáid darabszáma= {db2}")
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
        print("Te fogsz kezdeni,de előtte még meg akarom kérdezni azt,hogyha a robot 15 és 20 kozött húz lapot akkor egy bevállalós robotot vagy egy óvatos robotot szeretnél")
        print("Ennél a választásnál arról van szó,hogy a robot mennyi eséllyel húz fel még egy kártyát")
        eselykimutato = input("Szeretnéd látni az esélyeidet a különböző robotokkal?(i/n):")
        if eselykimutato == "i":
            print("A bevállalós robot: ha 16 akkor 75%,ha 17 akkor 60%,ha 18 akkor 45% ha 19 akkor 30% arra az esély,hogy felhúzzon még egy lapot ")
            print("könnyűnél a robot esélyei: ha 16 akkor 60%, ha 17 akkor 45% ha 18 akkor 30% ha 19 akkor 15%,hogy felhúzzon még egy lapot")
        else:
            print("")
        robotvalaszto = input("Egy bevállalós vagy egy óvatos robotot akarsz? (b/ó): ")
        print("A játékos:")
        kartyak1 = [randint(2, 11) for _ in range(2)]
        while sum(kartyak1) > 0 and sum(kartyak1) <= 16:
            kartyak1.append(randint(2, 11))
        print(f"A kártyáid száma = {kartyak1}")
        print(f"A kártyáid összege = {sum(kartyak1)}")
        if sum(kartyak1) > 16 and sum(kartyak1) < 20:
            ujrakero = input("Szeretnél húzni még egy kártyát?,(i,n):")
            if ujrakero == "i":
                kartyak1.append(randint(2, 11))
                sum(kartyak1)
                print(kartyak1)
            else:
                print("")
        db = len(kartyak1)
        vegsoszam = sum(kartyak1)
        print(f"A végső számod = {vegsoszam}")
        print(f"A kártyáid darabszáma= {db}")
        print("_______")
        print("A Robot:")
        kartyak2 = [randint(2, 11) for _ in range(2)]
        while sum(kartyak2) > 0 and sum(kartyak2) <= 16:
            kartyak2.append(randint(2, 11))
        print(f"A Robot száma = {kartyak2}")
        print(f"A Robot kártyái összege kártyáid összege = {sum(kartyak2)}")
        if sum(kartyak2) > 15 and sum(kartyak2)<20:
            ujrakerokartyak=[randint(1,100) for i in range(4)]
            if robotvalaszto =="b":
                if sum(kartyak2) == 16:
                    if ujrakerokartyak[0] <= 75:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 17:
                    if ujrakerokartyak[1]  <= 60:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 18:
                    if ujrakerokartyak[2] <= 45:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 19:
                    if ujrakerokartyak[3] <= 30:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                else:
                    print("")
            elif robotvalaszto =="ó":
                if sum(kartyak2) == 16:
                    if ujrakerokartyak[0] <= 60:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 17:
                    if ujrakerokartyak[1]  <= 45:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 18:
                    if ujrakerokartyak[2] <= 30:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                elif sum(kartyak2) == 19:
                    if ujrakerokartyak[3] <= 15:
                        print("A robot felhúzott még egy kártyát")
                        kartyak2.append(randint(2, 11))
                        sum(kartyak2)
                        print(f"A Robot kártyái száma = {kartyak2}")
                else:
                    print("")
            else:
                while robotvalaszto != "b" or "ó":
                    print("Csak ó-t vagy b-t írhatsz be")
                    robotvalaszto = input("Most tudsz választani,hogy bevállalós vagy egy óvatos robotot(b/ó): ")


        robotdb= len(kartyak2)
        masodikvegsoszam=sum(kartyak2)
        print(f"A robot végső száma:{masodikvegsoszam}")
        print(f"A robot végső kártyá száma:{robotdb}")

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


jatek = 'i'
while jatek == 'i':
    jatekmod = input("válassz játékmódot ember vagy robot(e,r): ")
    if jatekmod == "e":
        jatek_ember()
    elif jatekmod == "r":
        robot()
    else:
        print("Nem értelmezhető játékmód")

    if jatekmod in ("e", "r"):
        vegekerdes = ""
        while vegekerdes not in ('i', 'n'):
            vegekerdes = input("Szeretnél új játékot játszani? (i/n): ")
            if vegekerdes not in ('i', 'n'):
                print("Nem értelmezhető a válaszod, Csak i és n lehet")
            else:
                jatek = vegekerdes


