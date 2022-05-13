import json
import requests
import pprint

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = r.json()
bitcoin_usd = r["bpi"]["USD"]["rate_float"]
print(bitcoin_usd)