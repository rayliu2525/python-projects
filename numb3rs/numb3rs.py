import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_address = input("IPv4 Address: ")
    if re.search("^[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5].       $", ip_address)


...


if __name__ == "__main__":
    main()