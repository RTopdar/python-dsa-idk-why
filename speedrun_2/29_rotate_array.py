"""
29. Rotate Array  [Medium]  —  Arrays

Rotate `nums` to the right by `k` steps and return it. k can be larger than
len(nums).

Example:
    nums = [1, 2, 3, 4, 5, 6, 7], k = 3  ->  [5, 6, 7, 1, 2, 3, 4]

Bonus: do it in place with the "reverse 3 times" trick.
"""

from _runner import run_tests


def rotate(nums, k):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
    ("example 2", ([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
    ("k = 0", ([1, 2, 3], 0), [1, 2, 3]),
    ("k equals length", ([1, 2, 3], 3), [1, 2, 3]),
    ("k bigger than length", ([1, 2, 3], 4), [3, 1, 2]),
    ("single element", ([9], 5), [9]),
    ("empty list", ([], 3), []),
]


if __name__ == "__main__":
    run_tests(rotate, CASES)
