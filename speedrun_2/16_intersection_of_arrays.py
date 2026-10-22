"""
16. Intersection of Two Arrays  [Easy]  —  Sets

Return the unique values that appear in BOTH lists, sorted ascending.

Example:
    [1, 2, 2, 1], [2, 2]        ->  [2]
    [4, 9, 5], [9, 4, 9, 8, 4]  ->  [4, 9]
"""

from _runner import run_tests


def intersection(nums1, nums2):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 2, 2, 1], [2, 2]), [2]),
    ("example 2", ([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
    ("no overlap", ([1, 2], [3, 4]), []),
    ("one empty", ([], [1, 2]), []),
    ("identical lists", ([3, 1, 2], [2, 3, 1]), [1, 2, 3]),
    ("negatives", ([-1, -2, 0], [0, -2, 5]), [-2, 0]),
]


if __name__ == "__main__":
    run_tests(intersection, CASES)
