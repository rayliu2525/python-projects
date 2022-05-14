from plates import is_valid

def test_two_letters():
    assert is_valid("JK") == True

def test_num_middle():
    assert is_valid("JK00JK") == True