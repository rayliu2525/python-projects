from seasons import life_minutes

def normal_life_minutes():
    assert life_minutes("1992-02-25") == "Fifteen million, nine hundred twenty-four thousand, nine hundred sixty minutes"

def invalid_life_minutes():
    assert life_minutes("1992-January-25") == "Invalid date"

