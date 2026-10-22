"""
22. Majority Element  [Easy]  —  Dictionaries

Return the element that appears MORE than len(nums) // 2 times.
It is guaranteed to exist.

Example:
    [3, 2, 3]              ->  3
    [2, 2, 1, 1, 1, 2, 2]  ->  2

First solve with a dict, then try Boyer-Moore voting (O(1) space).
"""

from _runner import run_tests


def majority_element(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([3, 2, 3],), 3),
    ("example 2", ([2, 2, 1, 1, 1, 2, 2],), 2),
    ("single element", ([9],), 9),
    ("all same", ([4, 4, 4, 4],), 4),
    ("negative majority", ([-1, -1, 5],), -1),
    ("majority at the end", ([1, 2, 3, 3, 3],), 3),
]


if __name__ == "__main__":
    run_tests(majority_element, CASES)
