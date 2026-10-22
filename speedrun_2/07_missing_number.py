"""
07. Missing Number  [Easy]  —  Arrays / Sets / Math

`nums` has n distinct numbers taken from the range [0, n]. Exactly one number
from that range is missing. Return it.

Example:
    [3, 0, 1]  ->  2
    [0, 1]     ->  2

Try it two ways: with a set, and with the sum formula n*(n+1)//2.
"""

from _runner import run_tests


def missing_number(nums):
    num_hash = {}
    for index, value in enumerate(nums):
        num_hash[value]=index
    for i in range(max(nums)):
        if i not in num_hash:
            return i
    return max(nums)+1    


CASES = [
    ("example 1", ([3, 0, 1],), 2),
    ("example 2", ([0, 1],), 2),
    ("example 3", ([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
    ("missing zero", ([1],), 0),
    ("only zero present", ([0],), 1),
    ("missing middle, sorted", ([0, 1, 2, 4, 5],), 3),
]


if __name__ == "__main__":
    run_tests(missing_number, CASES)
