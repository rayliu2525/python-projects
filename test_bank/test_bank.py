from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("honk") == 20

def test_otherwise():
    assert value("adsdsf") == 100