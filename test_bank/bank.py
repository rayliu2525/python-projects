def main(greeting):
    dollar_amount = value(greeting)
    print(f"${dollar_amount}")


def value(greeting):
    x = input(f"{greeting}: ").lower().strip()

    if x[0:5] == "hello":
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main("hello")