"""
18. Happy Number  [Easy]  —  Sets / Loops

Start with a positive int n. Replace n with the sum of the squares of its
digits, and repeat. If it reaches 1 the number is happy (True). If it loops
forever without reaching 1, return False.

Example:
    19 -> 1^2+9^2=82 -> 68 -> 100 -> 1   ->  True
    2  -> loops forever                  ->  False

Hint: use a set of numbers already seen to detect the loop.
"""

from _runner import run_tests


def is_happy(n):
    # write your solution here
    pass


CASES = [
    ("example 1", (19,), True),
    ("example 2", (2,), False),
    ("one is happy", (1,), True),
    ("seven", (7,), True),
    ("four (the classic cycle)", (4,), False),
    ("big happy number", (1111111,), True),
    ("hundred", (100,), True),
]


if __name__ == "__main__":
    run_tests(is_happy, CASES)
