def main():
    dollar_amount = value()


def value(greeting):
    x = input("Type your greeting: ").lower().strip()

if x[0:5] == "hello":
    return 0
elif x[0] == "h":
    return 20
else:
    return 100


if __name__ == "__main__":
    main()