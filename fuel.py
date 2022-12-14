while True:

    try:

        x, y = input("enter an amount: " ).split("/")

    except ValueError:
        print("try again")
        continue

    try:
        if float(x).is_integer() == False or float(y).is_integer() == False:
            continue
    except ValueError:
        print("try again")
        continue

    x = int(x)
    y = int(y)

    try:
        gas_percent = f"{round(x / y * 100)}%"
    except ZeroDivisionError:
        print("try again")
        continue

    if x > y:
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

