import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if re.search("<iframe.*youtube.com.*</iframe>", s):
        match = re.search("src=", s)
        URL_start_index = match.end() + 1
        URL_end_index = s.find("\"", URL_start_index)
        URL = s[URL_start_index:URL_end_index]
        short_URL = URL.replace("be.com/embed", ".be")
        short_URL = short_URL.replace("http", "https")
        return short_URL
    else:
        return None


...


if __name__ == "__main__":
    main()