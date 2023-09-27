import pytest

def puissance(a, b):
    if b == 0:
        raise ZeroDivisionError("L'exposant ne peut pas être zéro.")
    try:
        result = int(a) ** int(b)
        return result
    except ValueError:
        raise ValueError("Les valeurs de la base et de l'exposant doivent être des nombres entier.")
