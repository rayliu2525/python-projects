


while True:

    x, y = input("enter an amount: " ).split(/)
    x = int(x)
    y = int(y)
    gas_percent = round(x / y * 100)

    try:
        x / y
    except (ZeroDivisionError):
        print("try again")
        continue

    if (x / y).isInteger() == False: or x > y
        raise ValueError:
            print("try again")
            continue

    elif x / y * 100 < 1:
        print("E)
        break

    elif x / y * 100 > 99:
        print("F")
        break

    else:
        print(gas_percent)
        break

