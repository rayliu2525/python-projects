from bank import value

def test_hello():
    assert value("hEllo") == 0

def test_h():
    assert value("honk") == 20

def test_otherwise():
    assert value("adDDFsdsf") == 100