from datetime import date
import re
import sys


def main():
    dob = input("Date of Birth: ")
    if re.search("^[1-9]{4}-[1-9]{2}-[1-9]{2}$", dob)
        sys.exit("Invaid date")
...


if __name__ == "__main__":
    main()