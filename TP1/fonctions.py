def puissance(a, b):
    try:
        return a ** b
    except TypeError:
        raise TypeError("Only integers are allowed")
