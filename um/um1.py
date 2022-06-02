import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    if re.

    matches = re.finditer("[^a-zA-Z]ums[^a-zA-Z]", s, re.IGNORECASE)
    matches1 = re.finditer("ums[^a-zA-Z]", s, re.IGNORECASE)


    matches = tuple(matches)
    return len(matches)


...


if __name__ == "__main__":
    main()