import pytest

def puissance(a, b):
    a, b = int(a), int(b)
    if not isinstance(b, int):
        raise ValueError("La valeur de l'exposant doit être un nombre entier.")
    if b == 0:
        raise ZeroDivisionError("L'exposant ne doit pas être 0.")
    if b <= 0:
        raise ValueError("L'exposant doit être un nombre entier positif.")
    try:
        result = int(a) ** int(b)
        return result
    except ValueError:
        raise ValueError("Les valeurs de la base et de l'exposant doivent être des nombres entiers.")
