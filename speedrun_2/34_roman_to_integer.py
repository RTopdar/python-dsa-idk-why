"""
34. Roman to Integer  [Easy]  —  Dictionaries / Loops

Convert a Roman numeral to an int.
I=1 V=5 X=10 L=50 C=100 D=500 M=1000.
If a smaller value comes before a larger one, subtract it (IV = 4, CM = 900).

Example:
    "III"      ->  3
    "LVIII"    ->  58
    "MCMXCIV"  ->  1994
"""

from _runner import run_tests


def roman_to_int(s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("III",), 3),
    ("example 2", ("LVIII",), 58),
    ("example 3", ("MCMXCIV",), 1994),
    ("single symbol", ("M",), 1000),
    ("subtract at start", ("IV",), 4),
    ("nine", ("IX",), 9),
    ("max value", ("MMMCMXCIX",), 3999),
]


if __name__ == "__main__":
    run_tests(roman_to_int, CASES)
