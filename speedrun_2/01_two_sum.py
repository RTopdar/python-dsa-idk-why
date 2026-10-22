"""
01. Two Sum  [Easy]  —  Arrays / Dictionaries

Given a list of ints `nums` and an int `target`, return the indices [i, j]
(i < j) of the two numbers that add up to target.
Exactly one valid answer exists. Don't use the same element twice.

Example:
    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]

Goal: O(n) with a dict (value -> index).
"""

from _runner import run_tests


def two_sum(nums, target):
    sum_hash = {}
    for index, value in enumerate(nums):
        complement = target-value
        if complement in sum_hash:
            return [sum_hash[complement], index]
        sum_hash[value] = index


CASES = [
    ("example 1", ([2, 7, 11, 15], 9), [0, 1]),
    ("example 2", ([3, 2, 4], 6), [1, 2]),
    ("same value twice", ([3, 3], 6), [0, 1]),
    ("negative numbers", ([-1, -2, -3, -4, -5], -8), [2, 4]),
    ("zeros", ([0, 4, 3, 0], 0), [0, 3]),
    ("answer at the end", ([1, 2, 3, 4, 5, 6], 11), [4, 5]),
    ("large values", ([1000000000, 5, -999999999], 1), [0, 2]),
]


if __name__ == "__main__":
    run_tests(two_sum, CASES)
