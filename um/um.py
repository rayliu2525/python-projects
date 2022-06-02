import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.finditer(r"\bum\b", s, re.IGNORECASE)
    matches = tuple(matches)
    return len(matches)


...


if __name__ == "__main__":
    main()