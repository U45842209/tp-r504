import pytest

def puissance(a, b):
    if b == 0:
        raise ZeroDivisionError("L'exposant ne peut pas être zéro.")
    if b < 0:
        raise ValueError("La valeur de l'exposant doit être un nombre entier positif.")
    try:
        result = int(a) ** int(b)
        return result
    except ValueError:
        raise ValueError("Les valeurs de la base et de l'exposant doivent être des nombres entier.")
