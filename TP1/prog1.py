import fonctions as f
import pytest



print("Hello , World !")

while True:
    number = int(input("Donnez un nombre : "))
    try:
        print(f"Voici le nombre au carré : {number**3}")
    except TypeError:
        print("Only integers are allowed")
        break
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"La fonction retroune : {f.puissance(number, 3)}")
