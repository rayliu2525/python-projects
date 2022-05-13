import json
import requests

r = requests.get('https://api.github.com/events')
r = json.dumps(r.text)
bitcoin_usd = r["bpi"]["USD"]["rate_float"]
print(bitcoin_usd)