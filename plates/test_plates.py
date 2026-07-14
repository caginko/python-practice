"""
Test suite for plates.py
Run with: pytest test_plates.py -v
"""

from plates import (
    is_valid,
    has_valid_length,
    starts_with_two_letters,
    is_alphanumeric,
    numbers_are_well_formed,
)


def test_valid_plates():
    assert is_valid("CS50") is True
    assert is_valid("AB") is True
    assert is_valid("AAA111") is True
    assert is_valid("CS") is True
    assert is_valid("AB1") is True


def test_invalid_length():
    assert is_valid("A") is False          # too short
    assert is_valid("ABCDEFG") is False     # too long (7 chars)


def test_must_start_with_two_letters():
    assert is_valid("1CS50") is False       # starts with a number
    assert is_valid("A1B2C3") is False      # second char is a digit


def test_alphanumeric_only():
    assert is_valid("CS 50") is False       # contains a space
    assert is_valid("CS-50") is False       # contains punctuation


def test_leading_zero_in_number_block():
    assert is_valid("CS05") is False        # leading zero
    assert is_valid("CS50") is True         # no leading zero, valid


def test_letters_cannot_follow_numbers():
    assert is_valid("CS50A") is False       # letter after digits started


def test_helper_functions_directly():
    assert has_valid_length("CS50") is True
    assert has_valid_length("A") is False

    assert starts_with_two_letters("CS50") is True
    assert starts_with_two_letters("1S50") is False

    assert is_alphanumeric("CS50") is True
    assert is_alphanumeric("CS 50") is False

    assert numbers_are_well_formed("CS50") is True
    assert numbers_are_well_formed("CS05") is False
    assert numbers_are_well_formed("CS50A") is False
