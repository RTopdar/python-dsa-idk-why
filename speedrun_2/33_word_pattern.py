"""
33. Word Pattern  [Easy]  —  Dictionaries / Strings

Given a `pattern` like "abba" and a string `s` of space-separated words,
return True if s follows the pattern: each letter maps to exactly one word
and each word maps to exactly one letter.

Example:
    "abba", "dog cat cat dog"   ->  True
    "abba", "dog cat cat fish"  ->  False
    "aaaa", "dog cat cat dog"   ->  False
"""

from _runner import run_tests


def word_pattern(pattern, s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("abba", "dog cat cat dog"), True),
    ("example 2", ("abba", "dog cat cat fish"), False),
    ("example 3", ("aaaa", "dog cat cat dog"), False),
    ("two letters one word", ("abba", "dog dog dog dog"), False),
    ("length mismatch", ("aaa", "dog dog"), False),
    ("single", ("a", "hello"), True),
]


if __name__ == "__main__":
    run_tests(word_pattern, CASES)
