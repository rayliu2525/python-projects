from project import *

def test_convert():
    assert convert("50") == 50

def test_end_balance():
    assert end_balance(100, .1, 2) == 120

def test_final_statement():
    assert final_statement(100) == f"You have {100}!"