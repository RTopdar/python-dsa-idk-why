"""
39. Set Mismatch  [Easy]  —  Sets / Arrays

`nums` should contain 1..n exactly once, but one number got duplicated and
replaced another. Return [duplicated, missing].

Example:
    [1, 2, 2, 4]  ->  [2, 3]
    [1, 1]        ->  [1, 2]
"""

from _runner import run_tests


def find_error_nums(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 2, 2, 4],), [2, 3]),
    ("example 2", ([1, 1],), [1, 2]),
    ("missing first", ([2, 2],), [2, 1]),
    ("unsorted", ([3, 2, 3, 4, 6, 5],), [3, 1]),
    ("missing last", ([1, 2, 3, 3],), [3, 4]),
]


if __name__ == "__main__":
    run_tests(find_error_nums, CASES)
