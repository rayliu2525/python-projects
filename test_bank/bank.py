def main():
    ...


def value(greeting):
    x = input("Type your greeting: ").lower().strip()

if x[0:5] == "hello":
    return 0
elif x[0] == "h":
    print("$20")
else:
    print("$100")


if __name__ == "__main__":
    main()