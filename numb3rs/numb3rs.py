import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_address = input("IPv4 Address: ")
    if re.search("^[1-9]$", ip_address)


...


if __name__ == "__main__":
    main()