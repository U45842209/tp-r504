def puissance(a, b):
    try:
        pow = 1
        for x in range(b):
            pow = pow*a
        return pow
    except TypeError:
        raise TypeError("Only integers are allowed")
