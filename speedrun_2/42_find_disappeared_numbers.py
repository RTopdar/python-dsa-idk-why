"""
42. Find All Disappeared Numbers  [Easy]  —  Sets / Arrays

`nums` has n numbers, each in range 1..n. Some appear twice, some are
missing. Return the missing numbers in ascending order.

Example:
    [4, 3, 2, 7, 8, 2, 3, 1]  ->  [5, 6]
"""

from _runner import run_tests


def find_disappeared(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([4, 3, 2, 7, 8, 2, 3, 1],), [5, 6]),
    ("example 2", ([1, 1],), [2]),
    ("nothing missing", ([2, 1, 3],), []),
    ("empty", ([],), []),
    ("all same", ([3, 3, 3],), [1, 2]),
]


if __name__ == "__main__":
    run_tests(find_disappeared, CASES)
