# python-practice

A growing collection of small Python exercises — input validation, string parsing, data structures, and general problem-solving. Each project includes a full pytest test suite.

## Structure

Each exercise lives in its own folder with its script and matching tests:

```
python-practice/
├── plates/
│   ├── plates.py
│   └── test_plates.py
├── fuel/
│   ├── fuel.py
│   └── test_fuel.py
└── README.md
```

## Projects

### 🚗 `plates/` — Vanity Plate Validator

Validates whether a license plate string follows a set of formatting rules:

- 2 to 6 characters long
- Must start with at least two letters
- Only letters and numbers allowed (no spaces or symbols)
- Numbers must come after all letters, and can't start with a leading zero

**Example:**
```
Plate: CS50
Valid

Plate: CS05
Invalid
```

**Run it:**
```bash
python plates/plates.py
```

**Run tests:**
```bash
pytest plates/test_plates.py -v
```

---

### ⛽ `fuel/` — Fuel Gauge

Converts a fraction (e.g. `"3/4"`) into a fuel gauge reading:

- `E` if the tank is essentially empty (≤ 1%)
- `F` if the tank is essentially full (≥ 99%)
- A percentage (e.g. `75%`) otherwise

Handles invalid input (bad formatting, division by zero, out-of-range fractions) by re-prompting the user.

**Example:**
```
Fraction: 1/4
25%

Fraction: 1/400
E
```

**Run it:**
```bash
python fuel/fuel.py
```

**Run tests:**
```bash
pytest fuel/test_fuel.py -v
```

*(Or just run `pytest` from the repo root to run every test suite at once.)*

---

## Setup

Requires Python 3.10+ and pytest:

```bash
pip install pytest
```

Clone the repo and run any script or its tests directly — no other dependencies needed. New exercises will be added over time, each in its own folder following the same pattern.

## What these demonstrate

- Input validation and defensive parsing
- Custom exception handling (`ValueError`, `ZeroDivisionError`)
- Breaking logic into small, single-purpose, testable functions
- Full unit test coverage with `pytest`, including edge cases
