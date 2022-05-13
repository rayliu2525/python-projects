import json
import requests
import pprint

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = json.dumps(r)
print(r)