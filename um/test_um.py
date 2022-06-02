from um import count

def test_separate_um():
    assert count("hello, um, um, hello") == 2

def test_substring_um():
    assert count("hello, hum, um, hello") == 1

def test_isolated_um():
    assert count("hello, hum uum m hello") == 2