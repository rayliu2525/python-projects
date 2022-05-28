import re
from numb3rs import validate

def test_valid():
    assert validate("1.1.1.1") == True

def test_invalid():
    assert validate("1.1.1.") == False