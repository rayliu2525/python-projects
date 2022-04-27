while True:

    x, y = input("enter an amount: " ).split("/")

    if float(x).is_integer() == False or float(y).is_integer() == False:
        continue

    x = int(x)
    y = int(y)
    gas_percent = round(x / y * 100)

    try:
        x / y
    except (ZeroDivisionError):
        print("try again")
        continue

    if x > y:
        raise ValueError:
            print("try again")
            continue

    elif x / y * 100 < 1:
        print("E")
        break

    elif x / y * 100 > 99:
        print("F")
        break

    else:
        print(gas_percent)
        break

