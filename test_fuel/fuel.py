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
        gas_percent = f"{round(x / y * 100)}%"
    except ZeroDivisionError:
        print("try again")
        return


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()