import sys
import requests

try:
    bitcoin_number = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit
except ValueError:
    print("Command-line argument is not a number")
    sys.exit

try:
    r = requests.get('https://api.github.com/events')
except requests.RequestException:
    print("error")

bitcoin_usd = r["bpi"]["USD"]["rate_float"]
total_amount = bitcoin_number * bitcoin_usd

total_amount = '{0:.4f}'.format(total_amount)
total_amount + '{:,}'.format(total_amount)
total_amount = float(total_amount)
print(total_amount)