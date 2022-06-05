from seasons import life_minutes

def normal_main():
    assert life_minutes("1992-02-25") == "Fifteen million, nine hundred and twenty-three thousand, five hundred and twenty minutes"

def invalid_main():
    assert life_minutes("1992-January-25") == "Invalid date"