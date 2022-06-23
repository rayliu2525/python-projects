from project import *

def test_convert():
    assert convert("50") == 50

def test_end_balance():
    assert end_balance(100, .1, 2) = 121