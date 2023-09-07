def puissance(a, b):
    try:
        pow = 1
        for x in range(b):
            pow = pow*a
        if a > 0:
            return pow
        elif a == 0:
            return 0
        else:
            return f"-{pow}"
        return pow
    except TypeError:
        raise TypeError("Only integers are allowed")
