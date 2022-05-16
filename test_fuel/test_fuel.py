from fuel import convert, gauge

def test_convert_full():
    assert convert("3/4") == 75

def test_convert_full():
    with pytest.raises(ZeroDivisionError) as info:
        raise ZeroDivisionError("try again")