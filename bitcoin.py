import sys
import requests

try:
    float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit
except ValueError:
    print("Command-line argument is not a number")
    sys.exit