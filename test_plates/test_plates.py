from plates import is_valid

def test_two_letters():
    assert is_valid("JK") == True

def test_num_end():
    assert is_valid("JK00") == True

def test_punctuations():
    assert is_valid("JK00!") == False

