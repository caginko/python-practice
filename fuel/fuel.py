"""
Fuel Gauge
----------
Reads a fuel fraction (e.g. "3/4") from the user and displays it as a
fuel gauge reading:

- "E"      if the tank is essentially empty (1% or less)
- "F"      if the tank is essentially full (99% or more)
- "NN%"    otherwise, rounded to the nearest whole percent

Keeps re-prompting until a valid fraction (X/Y where 0 <= X <= Y and
Y != 0) is entered.
"""


def main() -> None:
    while True:
        user_input = input("Fraction: ")
        try:
            percentage = convert(user_input)
        except (ValueError, ZeroDivisionError):
            continue
        print(gauge(percentage))
        break


def convert(fraction: str) -> int:
    """
    Convert a string like "3/4" into a whole-number percentage (0-100).

    Raises:
        ValueError: if the input isn't in "X/Y" integer form,
                    or if X is negative, or if X > Y (over 100%).
        ZeroDivisionError: if Y is 0.
    """
    try:
        numerator_str, denominator_str = fraction.split("/")
        numerator = int(numerator_str)
        denominator = int(denominator_str)
    except ValueError:
        # Covers: no "/" in input, more than one "/", or non-integer parts.
        raise ValueError("Fraction must be in the form X/Y with integers X, Y")

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be 0")

    if numerator < 0 or numerator > denominator:
        raise ValueError("Fraction must satisfy 0 <= X <= Y")

    return round((numerator / denominator) * 100)


def gauge(percentage: int) -> str:
    """Turn a 0-100 percentage into a gauge reading."""
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
