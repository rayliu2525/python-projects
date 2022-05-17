from fuel import convert, gauge

def test_convert_normal():
    assert convert("3/4") == 75

def test_gauge_full():
    assert gauge("100") == "F"

def test_gauge_empty():
    assert gauge("0") == "E"

def test_gauge_nomral():
    assert gauge("75") == "75%"
