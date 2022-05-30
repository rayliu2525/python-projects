import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("src=", s)
    URL_start_index = match.end() + 1
    s.find(", )



...


if __name__ == "__main__":
    main()