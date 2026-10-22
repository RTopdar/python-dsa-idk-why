"""
36. Find Pivot Index  [Easy]  —  Arrays / Prefix sum

The pivot index is where the sum of everything strictly to its left equals
the sum of everything strictly to its right. Return the LEFTMOST pivot index,
or -1 if none exists.

Example:
    [1, 7, 3, 6, 5, 6]  ->  3   (1+7+3 = 11 = 5+6)
    [1, 2, 3]           -> -1
    [2, 1, -1]          ->  0   (left sum is 0)
"""

from _runner import run_tests


def pivot_index(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 7, 3, 6, 5, 6],), 3),
    ("example 2", ([1, 2, 3],), -1),
    ("pivot at start", ([2, 1, -1],), 0),
    ("pivot at end", ([-1, 1, 5],), 2),
    ("single element", ([10],), 0),
    ("empty list", ([],), -1),
    ("all zeros -> leftmost", ([0, 0, 0],), 0),
]


if __name__ == "__main__":
    run_tests(pivot_index, CASES)
