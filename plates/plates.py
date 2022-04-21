def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0] and s[1] in ascii_uppercase:
        if 2 <= len(s) <= 6:
            for char in s:


            else:
                # make sure all are uppercase if no numbers
                return True

def num_at_end(s):
    for char in s:
        if char == range(0,10):
            


main()