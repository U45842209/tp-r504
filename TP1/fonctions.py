import pytest

def puissance(a, b):
    try:
        result = int(a) ** int(b)
        return result
    except ValueError:
        raise ValueError("Les valeurs de la base et de l'exposant doivent être des nombres entier.")
    except ZeroDivisionError:
        raise ValueError("L'exposant ne peut pas être zéro.")
