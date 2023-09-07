def puissance(a, b):
    if type(a) is not int and type(b) is not int:
        raise TypeError("Only integers are allowed")
    else:
        return a**b
