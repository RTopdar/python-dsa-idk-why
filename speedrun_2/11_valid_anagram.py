"""
11. Valid Anagram  [Easy]  —  Strings / Dictionaries

Return True if `t` is an anagram of `s` (same letters, same counts).

Example:
    s = "anagram", t = "nagaram"  ->  True
    s = "rat",     t = "car"      ->  False

Try with a dict of counts (no sorting, no Counter) first.
"""

from _runner import run_tests


def is_anagram(s, t):
    # write your solution here
    pass


CASES = [
    ("example 1", ("anagram", "nagaram"), True),
    ("example 2", ("rat", "car"), False),
    ("different lengths", ("ab", "abb"), False),
    ("both empty", ("", ""), True),
    ("same letters, wrong counts", ("aacc", "ccac"), False),
    ("case sensitive", ("Abc", "abc"), False),
    ("single char", ("a", "a"), True),
]


if __name__ == "__main__":
    run_tests(is_anagram, CASES)
