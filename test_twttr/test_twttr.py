from twttr import shorten

def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_numbers():
    assert shorten("AEIOUaeiou123") == "123"