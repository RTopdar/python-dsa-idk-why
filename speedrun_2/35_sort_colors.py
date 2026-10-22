"""
35. Sort Colors  [Medium]  —  Arrays / Two pointers

`nums` contains only 0, 1 and 2. Sort it in place (return it too) WITHOUT
using sort().

Example:
    [2, 0, 2, 1, 1, 0]  ->  [0, 0, 1, 1, 2, 2]

Easy way: count each value. Better: Dutch National Flag (low/mid/high), 1 pass.
"""

from _runner import run_tests


def sort_colors(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([2, 0, 2, 1, 1, 0],), [0, 0, 1, 1, 2, 2]),
    ("example 2", ([2, 0, 1],), [0, 1, 2]),
    ("single", ([1],), [1]),
    ("empty", ([],), []),
    ("already sorted", ([0, 1, 2],), [0, 1, 2]),
    ("all twos", ([2, 2, 2],), [2, 2, 2]),
    ("reverse", ([2, 2, 1, 1, 0, 0],), [0, 0, 1, 1, 2, 2]),
]


if __name__ == "__main__":
    run_tests(sort_colors, CASES)
