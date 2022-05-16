from fuel import convert, gauge

def test_convert_full():
    assert convert("3/4") == 75

def test_convert_full():
    assert convert("3/0") == ZeroDivisionError