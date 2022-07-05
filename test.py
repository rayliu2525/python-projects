def is_square(n):
    from math import sqrt
    try:
        if float(sqrt(n)).is_integer():
            return True
        else:
            return False
    except:
        return False

print(is_square(-1))