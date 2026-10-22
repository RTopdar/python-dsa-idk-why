"""
12. First Unique Character  [Easy]  —  Strings / Dictionaries

Return the index of the first character in `s` that appears exactly once.
Return -1 if there is none.

Example:
    "leetcode"      ->  0
    "loveleetcode"  ->  2
    "aabb"          -> -1
"""

from _runner import run_tests


def first_unique_char(s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("leetcode",), 0),
    ("example 2", ("loveleetcode",), 2),
    ("no unique", ("aabb",), -1),
    ("empty string", ("",), -1),
    ("single char", ("z",), 0),
    ("unique at the end", ("aabbc",), 4),
    ("spaces count too", ("a a",), 1),
]


if __name__ == "__main__":
    run_tests(first_unique_char, CASES)
