from twttr import shorten

def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""
