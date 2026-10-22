"""
38. Jewels and Stones  [Easy]  —  Sets / Strings

`jewels` lists the jewel types (each char is a type). `stones` is what you
have. Count how many of your stones are jewels. Case sensitive.

Example:
    jewels = "aA", stones = "aAAbbbb"  ->  3
"""

from _runner import run_tests


def num_jewels(jewels, stones):
    # write your solution here
    pass


CASES = [
    ("example 1", ("aA", "aAAbbbb"), 3),
    ("case sensitive", ("z", "ZZ"), 0),
    ("no jewels", ("", "abc"), 0),
    ("no stones", ("abc", ""), 0),
    ("all jewels", ("ab", "abba"), 4),
]


if __name__ == "__main__":
    run_tests(num_jewels, CASES)
