from seasons import life_minutes

def test_normal_life_minutes():
    assert life_minutes("1992-02-25") == "Fifteen million, nine hundred twenty-four thousand, nine hundred sixty minutes"

def test_invalid_life_minutes():
    assert life_minutes("1992-January-25") == "Invalid date"