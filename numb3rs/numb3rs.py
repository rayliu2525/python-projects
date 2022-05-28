import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_address = input("IPv4 Address: ")
    if re.search("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip_address):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()