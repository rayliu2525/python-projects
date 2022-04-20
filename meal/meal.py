def main():
    ...


def convert(time):
    x, y = time.split(":")
    y = int(y)/60
    return x + y


if __name__ == "__main__":
    main()