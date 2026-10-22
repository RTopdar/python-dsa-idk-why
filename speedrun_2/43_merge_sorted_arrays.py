"""
43. Merge Two Sorted Arrays  [Easy]  —  Arrays / Two pointers

Merge two sorted lists into one sorted list. Don't use sort() / sorted().

Example:
    [1, 2, 4], [1, 3, 4]  ->  [1, 1, 2, 3, 4, 4]

Hint: two pointers i, j; append leftovers at the end.
"""

from _runner import run_tests


def merge_sorted(a, b):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    ("first empty", ([], [1, 2]), [1, 2]),
    ("second empty", ([5], []), [5]),
    ("both empty", ([], []), []),
    ("no interleave", ([1, 2], [3, 4]), [1, 2, 3, 4]),
    ("negatives", ([-5, 0, 3], [-2, 8]), [-5, -2, 0, 3, 8]),
]


if __name__ == "__main__":
    run_tests(merge_sorted, CASES)
