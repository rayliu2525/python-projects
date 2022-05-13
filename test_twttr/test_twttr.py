import twttr

def test_shorten3():
    x = twttr.shorten("AEIOUaeiou")
    if x == "":
        return True
    else:
        return False
