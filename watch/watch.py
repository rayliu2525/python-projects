import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("src=", s)
    URL_start_index = match.end() + 2
    URL_end_index = s.find("\"", URL_start_index + 1)
    URL = s[URL_start_index:URL_end_index + 1]
    short_URL = s.replace("be.com/embed", ".be")
    return short_URL


...


if __name__ == "__main__":
    main()