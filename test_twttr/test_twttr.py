from twttr import shorten

def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_numbers():
    assert shorten("AEIOUaeiou123") == "123"

def test_upper():
    assert shorten("AENTYTY!ad") == "NTYTY!d"

def test_upper():
    assert shorten("AEN!") == "N!"