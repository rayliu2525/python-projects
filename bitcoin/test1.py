import json
import requests

r = requests.get('https://api.github.com/events')
r = r.json()
bitcoin_usd = r["bpi"]["USD"]["rate_float"]
print(bitcoin_usd)