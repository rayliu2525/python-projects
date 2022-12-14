import pytest

from fuel import convert, gauge

def test_convert_normal():
    assert convert("3/4") == 75

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_nomral():
    assert gauge(75) == "75%"