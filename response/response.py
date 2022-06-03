from validator_collection import validators

def main():
    print(validate(input("Type Email: ")))

def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()