"""
44. Longest Repeating Character Replacement  [Medium]  —  Strings / Dictionaries / Sliding window

`s` is uppercase letters. You may change at most `k` characters to any other
letter. Return the length of the longest substring of one repeated letter you
can get.

Example:
    s = "ABAB",    k = 2  ->  4   (change both A's or both B's)
    s = "AABABBA", k = 1  ->  4   ("AABA" -> "AAAA")

Hint: window is valid while (window_len - max_count_in_window) <= k.
"""

from _runner import run_tests


def character_replacement(s, k):
    # write your solution here
    pass


CASES = [
    ("example 1", ("ABAB", 2), 4),
    ("example 2", ("AABABBA", 1), 4),
    ("k = 0", ("AABBB", 0), 3),
    ("empty", ("", 2), 0),
    ("k bigger than string", ("ABC", 5), 3),
    ("single char", ("A", 0), 1),
    ("all same", ("BBBB", 1), 4),
]


if __name__ == "__main__":
    run_tests(character_replacement, CASES)
