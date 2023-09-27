import pytest

def puissance(a, b):
    a, b = int(a), int(b)
    if b == int:
        if b < 0:
            raise ValueError("La valeur de l'exposant doit être un nombre entier positif.")
        if b == 0:
            raise ZeroDivisionError("L'exposant ne peut pas être zéro.")
    if b != int:
        raise ValueError("La valeur de l'exposant doit être un nombre.")
    try:
        result = int(a) ** int(b)
        return result
    except ValueError:
        raise ValueError("Les valeurs de la base et de l'exposant doivent être des nombres entier.")
