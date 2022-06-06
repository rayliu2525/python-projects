from seasons import life_minutes
import pytest

def test_normal_life_minutes():
    assert life_minutes("1992-02-25") == "Fifteen million, nine hundred twenty-four thousand, nine hundred sixty minutes"

def test_error():
    with pytest.raises(SystemExit):
        life_minutes("1992-January-25")