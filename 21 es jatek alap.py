from random import randint

print("Üdvözöllek a 21 es játékba✨")
print("A cél az  közelebb legyen a 21-hez")
print("Ebben a játékban a lapo száma 1 és  10 között lesz")
print("3 kártyád van")
print("A kártyáidat össze is tudod adni")
ellenfelvalaszto=input("Robot ellen vagy ember ellen szeretnél játszani?(robot/ember):")
if ellenfelvalaszto == "ember":
    print("Akkor Ember ellen szeretnél játszani")
    kartyaszam4 = randint(1, 10)
    kartyaszam5 = randint(1, 10)
    kartyaszam6 = randint(1, 10)
    print("Az első játékos")
    kartyak = {
            "kartya1": f"{kartyaszam4}",
            "kartya2": f"{kartyaszam5}",
            "kartya3":f"{kartyaszam6}"
        }
    print(kartyak)
    print(f"A kártyáid száma={kartyaszam4+kartyaszam5+kartyaszam6}")
    kivonas=input("Ezek közül melyikeket szeretnéd kivonni(persze ha szeretnél)példa:(1.kártya,2.kártya)ha nem akkor írd azt ,hogy (semmi):").lower()
    if kivonas == "1.kártya":
        vegsoszam=(kartyaszam5+kartyaszam6)
    elif kivonas =="2.kártya":
        vegsoszam=(kartyaszam4+kartyaszam6)
    elif kivonas =="3.kártya":
        vegsoszam=(kartyaszam4+kartyaszam5)
    elif kivonas=="semmi":
        vegsoszam=(kartyaszam4+kartyaszam5+kartyaszam6)
    else:
        print("Ide mást mint ('1.kártya','2.kártya',3.kártya','semmi')")
    print(f"a végső számod ={vegsoszam}")
    kartyaszam = randint(1, 10)
    kartyaszam2 = randint(1, 10)
    kartyaszam3 = randint(1, 10)
    print("A második játékos:")
    kartyak = {
            "kartya1": f"{kartyaszam}",
            "kartya2": f"{kartyaszam2}",
            "kartya3": f"{kartyaszam3}"
    }
    print(kartyak)
    print(f"A kártyáid száma={kartyaszam + kartyaszam2 + kartyaszam3}")
    kivonas = input("Ezek közül melyikeket szeretnéd kivonni(persze ha szeretnél)példa:(1.kártya,2.kártya)ha nem akkor írd azt ,hogy (semmi):").lower()
    if kivonas == "1.kártya":
            masodikvegsoszam = (kartyaszam2 + kartyaszam3)
    elif kivonas == "2.kártya":
            masodikvegsoszam = (kartyaszam + kartyaszam3)
    elif kivonas == "3.kártya":
            masodikvegsoszam = (kartyaszam + kartyaszam2)
    elif kivonas == "semmi":
            masodikvegsoszam = (kartyaszam + kartyaszam2 + kartyaszam3)
    else:
        print("Ide mást mint ('1.kártya','2.kártya',3.kártya','semmi')")
    print(f"a végső számod ={masodikvegsoszam}")
    if  vegsoszam> 21 and masodikvegsoszam > 21:
        print("Mindkét játékos túllépte a 21-et, döntetlen!")
    elif vegsoszam > 21:
        print("Az első játékos túllépte a 21-et, ezért a második játékos nyer!")
    elif masodikvegsoszam > 21:
        print("A második játékos túllépte a 21-et, ezért az első játékos nyer!")
    if vegsoszam > masodikvegsoszam:
        print("Az első játékos nyert")
    elif masodikvegsoszam >vegsoszam:
        print("A második játékos nyert")
    elif masodikvegsoszam == vegsoszam:
        print("Döntetlen")






elif ellenfelvalaszto== "robot":
    print("Akkor robot ellen szeretnél játszani")
else:
    while ellenfelvalaszto != "ember" or ellenfelvalaszto != "robot":
        print("Csak robottot vagy embert írhatsz be")
        ellenfelvalaszto = input("Robot ellen vagy ember ellen szeretnél játszani?(robot/ember):")
