from plates import is_valid

def test_two_letters():
    assert is_valid("AAA222") == True

def test_num_end():
    assert is_valid("JK50") == True

def test_punctuations():
    assert is_valid("JK00!") == False

