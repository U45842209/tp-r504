def puissance(a, b):
    try:
        pow = 1
        for x in range(b):
            pow = pow*a
        if a > 0:
            return pow
        elif a == 0:
            raise ValueError("This is not right")
        elif a == 0 and b == 0:
            return 1
        else:
            return int(f"-{pow}")

    except TypeError:
        raise TypeError("Only integers are allowed")
