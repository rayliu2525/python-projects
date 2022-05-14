from twttr import shorten

def test_shorten3():
    x = twttr.shorten("AEIOUaeiou")
    if x == "":
        return True
    else:
        return False
