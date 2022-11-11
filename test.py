from app import sum_digits


def test_sum_digits_no_entry():
    assert sum_digits() == 0


def test_sum_digits_one_digit():
    assert sum_digits(1) == 1


def test_sum_digits_two_digits():
    assert sum_digits(12) == 3


def test_sum_digits_three_digits():
    assert sum_digits(123) == 6
