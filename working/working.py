import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("^([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P:M) to ([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P:M)$", s):
        


    else:
        raise ValueError


...


if __name__ == "__main__":
    main()