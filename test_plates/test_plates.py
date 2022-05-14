from plates import is_valid

def test_two_letters():
    assert is_valid("222") == False

def test_num_end():
    assert is_valid("JK50K") == False

def test_punctuations():
    assert is_valid("JK00!") == False

def test_numbmiddle():
    assert is_valid("JK00K") == False

def test_length():
    assert is_valid("JKKKKKKK") == False

def test_zero():
    assert is_valid("0K") == False

def test_0():
    assert is_valid("JK50") == True