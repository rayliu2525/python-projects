from plates import is_valid

def test_two_letters():
    assert is_valid("222") == False

def test_num_end():
    assert is_valid("JK500000") == False

def test_punctuations():
    assert is_valid("JK00!") == False

