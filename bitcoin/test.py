import json
import requests

r = requests.get('https://api.github.com/events')
print(r.text["bpi"]["USD"]["rate_float"])