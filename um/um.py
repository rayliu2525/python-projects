import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.finditer("um", s, re.IGNORECASE)


...


if __name__ == "__main__":
    main()