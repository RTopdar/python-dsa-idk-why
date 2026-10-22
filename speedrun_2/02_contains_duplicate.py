"""
02. Contains Duplicate  [Easy]  —  Arrays / Sets

Return True if any value appears at least twice in `nums`, else False.

Example:
    [1, 2, 3, 1]  ->  True
    [1, 2, 3, 4]  ->  False
"""

from _runner import run_tests


def contains_duplicate(nums):
    # write your solution here
    return len((set(nums))) != len(nums)


CASES = [
    ("example 1", ([1, 2, 3, 1],), True),
    ("example 2", ([1, 2, 3, 4],), False),
    ("many duplicates", ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
    ("empty list", ([],), False),
    ("single element", ([7],), False),
    ("negatives + zero", ([-1, 0, 1, -1],), True),
    ("big unique range", (list(range(10000)),), False),
]


if __name__ == "__main__":
    run_tests(contains_duplicate, CASES)
