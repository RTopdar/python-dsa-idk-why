"""
17. Longest Consecutive Sequence  [Medium]  —  Sets

Given an unsorted list of ints, return the length of the longest run of
consecutive values (e.g. 1,2,3,4). Order in the list doesn't matter.

Example:
    [100, 4, 200, 1, 3, 2]  ->  4   (1, 2, 3, 4)

Goal: O(n) with a set — only start counting from numbers where n-1 is NOT
in the set.
"""

from _runner import run_tests


def longest_consecutive(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([100, 4, 200, 1, 3, 2],), 4),
    ("example 2", ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
    ("empty list", ([],), 0),
    ("single element", ([42],), 1),
    ("duplicates", ([1, 2, 2, 3],), 3),
    ("negatives", ([-3, -2, -1, 5, 6],), 3),
    ("no neighbours", ([10, 30, 50],), 1),
]


if __name__ == "__main__":
    run_tests(longest_consecutive, CASES)
