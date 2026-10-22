"""
32. Ransom Note  [Easy]  —  Dictionaries / Strings

Return True if `note` can be built using letters from `magazine`. Each
letter in magazine can be used only once.

Example:
    note = "aa", magazine = "aab"  ->  True
    note = "aa", magazine = "ab"   ->  False
"""

from _runner import run_tests


def can_construct(note, magazine):
    # write your solution here
    pass


CASES = [
    ("example 1", ("aa", "aab"), True),
    ("example 2", ("aa", "ab"), False),
    ("empty note", ("", "abc"), True),
    ("empty magazine", ("a", ""), False),
    ("exact same", ("hello", "olleh"), True),
    ("case sensitive", ("A", "a"), False),
]


if __name__ == "__main__":
    run_tests(can_construct, CASES)
