import re
import sys

def test_00_convert:
    assert convert("5:00 AM to 9:00 PM") = "5:00 to 21:00"