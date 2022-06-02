import re

def count(s):
    matches = re.finditer("[^a-zA-Z]ums[^a-zA-Z]", s, re.IGNORECASE)
    matches1 = re.finditer("ums[^a-zA-Z]", s, re.IGNORECASE)
    print(matches)
    print(matches1)

count("hello, hum um um hello")