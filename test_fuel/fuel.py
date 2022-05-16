def main(fraction):
    percentage = convert(fraction)
    x = gauge(percentage)
    print(x)


def convert(fraction):
    try:
        x, y = fraction.split("/")

    except ValueError:
        raise ValueError("try again")

    try:
        if float(x).is_integer() == False or float(y).is_integer() == False:
            return
    except ValueError:
        raise ValueError("try again")

    x = int(x)
    y = int(y)

    try:
        percentage = round(x / y * 100)
    except ZeroDivisionError:
        raise ZeroDivisionError("try again")

    if x > y:
        print("try again")
        return

    return percentage


def gauge(percentage):
    if percentage < 1:
        return "E"


    elif percentage > 99:
        return "F"


    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main("5.4/100")