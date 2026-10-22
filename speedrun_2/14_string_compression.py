"""
14. String Compression  [Easy]  —  Strings / Loops

Compress runs of the same character: write the char followed by the run
length. If the run length is 1, write only the char.

Example:
    "aabcccccaaa"  ->  "a2bc5a3"
    "abc"          ->  "abc"
"""

from _runner import run_tests


def compress(s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("aabcccccaaa",), "a2bc5a3"),
    ("no repeats", ("abc",), "abc"),
    ("empty string", ("",), ""),
    ("single char", ("a",), "a"),
    ("one long run", ("zzzzzzzzzzzz",), "z12"),
    ("same char split up", ("aabaa",), "a2ba2"),
    ("case sensitive", ("aAaa",), "aAa2"),
]


if __name__ == "__main__":
    run_tests(compress, CASES)
