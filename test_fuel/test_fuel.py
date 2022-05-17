from fuel import convert, gauge

def test_convert_normal():
    assert convert("3/4") == 75

def test_gauge_full():
    assert gauge("100") == "F"