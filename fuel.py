while True:

    x, y = input("enter an amount: " ).split(/)
    gas_percent = round(x / y * 100)

    try:
        x / y
    except (ZeroDivisionError):
        print("try again")

    if x / y * 100 < 1:
        print("E)
        break

    elif x > y:
        raise ValueError:
            print("try again")


    elif x / y * 100 > 99:
        print("F")
        break

    else:
        print(gas_percent)
        break

