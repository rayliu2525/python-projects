import re
import sys

def test_valid():
    assert validate("1.1.1.1") == True