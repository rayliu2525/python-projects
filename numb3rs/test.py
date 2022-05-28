import re

ip_address = input("IPv4 Address: ")
if re.search("^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]\.){3}([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip_address):
    print("True")
else:
    print("False")