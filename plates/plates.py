def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0] and s[1] in ascii_uppercase:
        if 2 <= len(s) <= 6:
            if s[2:] in range(0,10)

            else:
                # make sure all are uppercase if no numbers
                return True


main()