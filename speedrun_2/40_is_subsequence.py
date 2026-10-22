"""
40. Is Subsequence  [Easy]  —  Strings / Two pointers

Return True if `s` is a subsequence of `t`: you can delete some (or zero)
chars from t, without reordering, to get s.

Example:
    "abc", "ahbgdc"  ->  True
    "axc", "ahbgdc"  ->  False
"""

from _runner import run_tests


def is_subsequence(s, t):
    # write your solution here
    pass


CASES = [
    ("example 1", ("abc", "ahbgdc"), True),
    ("example 2", ("axc", "ahbgdc"), False),
    ("empty s", ("", "abc"), True),
    ("empty t", ("a", ""), False),
    ("both empty", ("", ""), True),
    ("order matters", ("ba", "abc"), False),
    ("repeated chars", ("aaa", "abaca"), True),
]


if __name__ == "__main__":
    run_tests(is_subsequence, CASES)
