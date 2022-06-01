from working import convert

def test_00_convert():
    assert convert("5:00 AM to 9:00 PM") == "05:00 to 21:00"

def test_nozero_convert():
    assert convert("5 AM to 9 PM") == "05:00 to 21:00"

def test_both24_convert():
    assert convert("9:00 PM to 11:00 PM") == "21:00 to 23:00"

def test_both24_convert():
    assert convert("9:00 PM - 11:00 PM") == "21:00 to 23:00"