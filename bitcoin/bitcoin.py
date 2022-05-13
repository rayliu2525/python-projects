import sys
import requests
import json

try:
    bitcoin_number = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit
except ValueError:
    print("Command-line argument is not a number")
    sys.exit

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print("error")

r = r.json()
bitcoin_usd = r["bpi"]["USD"]["rate_float"]
total_amount = bitcoin_number * bitcoin_usd

print(f"${total_amount:,.4f}")