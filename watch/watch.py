import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("src=", s)
    URL_start_index = match.end() + 1
    URL_end_index = s.find("\"", URL_start_index + 1)



...


if __name__ == "__main__":
    main()