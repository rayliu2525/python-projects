import json
import requests
import pprint

r = requests.get('https://api.github.com/events')
r = json.dumps(r.text)
r = json.loads(r)
pprint.pp(r)