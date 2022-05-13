import json
import requests

r = requests.get('https://api.github.com/events')
r = json.dumps(r.text)
r = json.loads(r)
print(r)