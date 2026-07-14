"""
Vanity Plate Validator
-----------------------
Checks whether a given license plate string follows these rules:

1. Length must be between 2 and 6 characters (inclusive).
2. Must start with at least two letters.
3. Must contain only letters and numbers (no spaces, punctuation, etc).
4. Numbers, if present, must all come after the letters, and the
   first number in the sequence cannot be a leading zero
   (e.g. "AB01" is valid, "AB0" is not, "AB10" is valid).

Example valid plates:  "CS50", "AB", "AAA111"
Example invalid plates: "1CS50" (starts with a number),
                        "CS 50" (contains a space),
                        "CS05" (leading zero in number block)
"""


def main() -> None:
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s: str) -> bool:
    """Run a candidate plate through all validation rules in order."""
    checks = (
        has_valid_length,
        starts_with_two_letters,
        is_alphanumeric,
        numbers_are_well_formed,
    )
    return all(check(s) for check in checks)


def has_valid_length(s: str) -> bool:
    """Plate must be 2 to 6 characters long."""
    return 2 <= len(s) <= 6


def starts_with_two_letters(s: str) -> bool:
    """First two characters must be letters.

    Assumes has_valid_length has already confirmed len(s) >= 2,
    so indexing s[1] here is always safe.
    """
    return s[0].isalpha() and s[1].isalpha()


def is_alphanumeric(s: str) -> bool:
    """No spaces, punctuation, or symbols allowed — letters and digits only."""
    return s.isalnum()


def numbers_are_well_formed(s: str) -> bool:
    """
    Digits must all appear together at the end of the plate
    (no letters after a digit appears), and the number block
    cannot start with '0'.
    """
    number_block_started = False

    for char in s:
        if char.isdigit():
            if not number_block_started and char == "0":
                return False
            number_block_started = True
        elif number_block_started:
            # A letter showed up after numbers had already started.
            return False

    return True


if __name__ == "__main__":
    main()
