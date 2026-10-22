"""
10. Reverse Words in a String  [Easy]  —  Strings

Reverse the order of words in `s`. Words are separated by one or more spaces.
Result must have single spaces between words and no leading/trailing spaces.

Example:
    "the sky is blue"     ->  "blue is sky the"
    "  hello world  "     ->  "world hello"
"""

from _runner import run_tests


def reverse_words(s):
    return " ".join(s.split()[::-1])


CASES = [
    ("example 1", ("the sky is blue",), "blue is sky the"),
    ("leading/trailing spaces", ("  hello world  ",), "world hello"),
    ("multiple spaces between", ("a good   example",), "example good a"),
    ("single word", ("python",), "python"),
    ("empty string", ("",), ""),
    ("only spaces", ("     ",), ""),
    ("punctuation stays with word", ("hi, there!",), "there! hi,"),
]


if __name__ == "__main__":
    run_tests(reverse_words, CASES)
