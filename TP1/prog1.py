import fonctions as f
import pytest



print("Hello , World !")

while True:
    number = input("Donnez un nombre : ")
    print(f"Voici le nombre au carré : {int(number)**2}")
    print("Or use the function")
    f.puissance(int(number), 2)
