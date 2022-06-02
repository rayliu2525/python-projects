import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.finditer("[^a-zA-Z]um[^a-zA-Z]", s, re.IGNORECASE)
    matches = tuple(matches)
    return len(matches)


...


if __name__ == "__main__":
    main()