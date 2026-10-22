"""
46. Find All Anagrams in a String  [Medium]  —  Strings / Dictionaries / Sliding window

Return the start indices of every substring of `s` that is an anagram of `p`
(in ascending order).

Example:
    s = "cbaebabacd", p = "abc"  ->  [0, 6]
    s = "abab",       p = "ab"   ->  [0, 1, 2]

Goal: fixed-size sliding window with a count dict — don't re-sort each window.
"""

from _runner import run_tests


def find_anagrams(s, p):
    # write your solution here
    pass


CASES = [
    ("example 1", ("cbaebabacd", "abc"), [0, 6]),
    ("example 2", ("abab", "ab"), [0, 1, 2]),
    ("p longer than s", ("a", "ab"), []),
    ("no match", ("hello", "xyz"), []),
    ("whole string", ("listen", "silent"), [0]),
    ("repeated letters", ("aaaa", "aa"), [0, 1, 2]),
]


if __name__ == "__main__":
    run_tests(find_anagrams, CASES)
