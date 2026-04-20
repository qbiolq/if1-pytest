from leap_year import is_leap_year

def test_pytest():
    assert 2 + 2 == 4

def test_is_leap_year_happy():
    assert is_leap_year(2000) == True

def test_is_leap_year_unhappy():
    assert is_leap_year(1900) == False