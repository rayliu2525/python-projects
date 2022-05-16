def main():
    ...


def convert(fraction):
    try:
        x, y = fraction.split("/")

    except ValueError:
        print("try again")
        return

    try:
        if float(x).is_integer() == False or float(y).is_integer() == False:
            pass
    except ValueError:
        print("try again")
        return

    x = int(x)
    y = int(y)

    try:
        percentage = round(x / y * 100)
    except ZeroDivisionError:
        print("try again")
        return

    if x > y:
        print("try again")
        return

    return percentage


def gauge(percentage):
    if percentage < 1:
        print("E")
        break

    elif x / y * 100 > 99:
        print("F")
        break

    else:
        print(gas_percent)
        break


if __name__ == "__main__":
    main()