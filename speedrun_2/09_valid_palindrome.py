"""
09. Valid Palindrome  [Easy]  —  Strings / Two pointers

A phrase is a palindrome if, after lowercasing and removing every
non-alphanumeric character, it reads the same forward and backward.
Return True / False.

Example:
    "A man, a plan, a canal: Panama"  ->  True
    "race a car"                      ->  False

Hint: str.isalnum(), str.lower()
"""

from _runner import run_tests


def is_palindrome(s):
    import re
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
    


CASES = [
    ("example 1", ("A man, a plan, a canal: Panama",), True),
    ("example 2", ("race a car",), False),
    ("only spaces", (" ",), True),
    ("empty string", ("",), True),
    ("digits matter", ("0P",), False),
    ("numeric palindrome", ("12321",), True),
    ("punctuation only", (".,!?",), True),
    ("mixed case", ("Was it a car or a cat I saw?",), True),
]


if __name__ == "__main__":
    run_tests(is_palindrome, CASES)
