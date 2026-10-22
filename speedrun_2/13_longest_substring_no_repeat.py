"""
13. Longest Substring Without Repeating Characters  [Medium]  —  Strings / Sets / Sliding window

Return the length of the longest substring of `s` with no repeated characters.

Example:
    "abcabcbb"  ->  3   ("abc")
    "bbbbb"     ->  1
    "pwwkew"    ->  3   ("wke")

Goal: O(n) sliding window with a set (or dict of last-seen index).
"""

from _runner import run_tests


def length_of_longest_substring(s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("abcabcbb",), 3),
    ("example 2", ("bbbbb",), 1),
    ("example 3", ("pwwkew",), 3),
    ("empty string", ("",), 0),
    ("single space", (" ",), 1),
    ("all unique", ("abcdef",), 6),
    ("repeat jumps back", ("abba",), 2),
    ("tricky window", ("dvdf",), 3),
]


if __name__ == "__main__":
    run_tests(length_of_longest_substring, CASES)
