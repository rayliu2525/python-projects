from validator-collection import validators

def main():
    print(validate(input("Type Email: ")))

def validate(s):
    if validate.email(s):
        return "Valid"
    else:
        return "Invalid"