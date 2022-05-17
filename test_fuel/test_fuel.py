from fuel import convert, gauge

def test_convert_normal():
    assert convert("3/4") == 75

def test_convert_full():
    assert convert("4/4") == 100