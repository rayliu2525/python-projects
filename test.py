def is_square(n):
    from math import sqrt
    if float(sqrt(n)).is_integer():
        return True
    else:
        return False