"""
Test suite for fuel.py
Run with: pytest test_fuel.py -v
"""

import pytest
from fuel import convert, gauge


def test_convert_valid_fractions():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_convert_rounds_correctly():
    assert convert("1/3") == 33   # 33.33... rounds to 33
    assert convert("2/3") == 67   # 66.66... rounds to 67


def test_convert_raises_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_raises_value_error_on_bad_format():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("not a fraction")


def test_convert_raises_value_error_on_out_of_range():
    with pytest.raises(ValueError):
        convert("-1/4")     # negative numerator
    with pytest.raises(ValueError):
        convert("5/4")      # numerator > denominator (over 100%)


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_normal_range():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
