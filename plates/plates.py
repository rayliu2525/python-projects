import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if only_letters_nums(s):
        if ascii_first_two(s):
            if 2 <= len(s) <= 6:
                if num_at_end(s):
                    return True
                if all_in_ascii(s):
                    return True
    else:
        return False

def num_at_end(s):
    for char in s:
        if char == range(0,10):
            if string.ascii_uppercase not in s[s.index[char]:]:
                return True

def all_in_ascii(s):
    for char in s:
        if char in string.ascii_uppercase:
            return True

def only_letters_nums(s):
    for char in s:
        if char not in string.ascii_uppercase and char not in range(0,10):
            return False
    return True

def ascii_first_two(s):
    if s[0] and s[1] in string.ascii_uppercase:
        return True
    else:
        return False

main()