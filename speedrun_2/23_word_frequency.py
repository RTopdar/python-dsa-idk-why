"""
23. Word Frequency  [Easy]  —  Dictionaries / Strings

Count how often each word appears in `text`. Words are case-insensitive and
these punctuation marks should be stripped: . , ! ?
Return a dict {word: count} with lowercase words.

Example:
    "The cat and the hat."  ->  {"the": 2, "cat": 1, "and": 1, "hat": 1}

Don't use collections.Counter — practice dict.get(key, 0).
"""

from _runner import run_tests


def word_frequency(text):
    # write your solution here
    pass


CASES = [
    ("example 1", ("The cat and the hat.",), {"the": 2, "cat": 1, "and": 1, "hat": 1}),
    ("empty string", ("",), {}),
    ("only punctuation", ("!?.,",), {}),
    ("mixed case", ("Go go GO",), {"go": 3}),
    ("extra spaces", ("  a   b  a ",), {"a": 2, "b": 1}),
    ("punctuation inside text", ("Hi! Hi, there? there.",), {"hi": 2, "there": 2}),
]


if __name__ == "__main__":
    run_tests(word_frequency, CASES)
