"""
25. Subarray Sum Equals K  [Medium]  —  Dictionaries / Prefix sum

Return how many contiguous subarrays of `nums` sum to exactly `k`.

Example:
    nums = [1, 1, 1], k = 2  ->  2
    nums = [1, 2, 3], k = 3  ->  2   ([1,2] and [3])

Goal: O(n) with a dict {prefix_sum: times_seen}. Start it with {0: 1}.
"""

from _runner import run_tests


def subarray_sum(nums, k):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 1, 1], 2), 2),
    ("example 2", ([1, 2, 3], 3), 2),
    ("negatives", ([1, -1, 0], 0), 3),
    ("no match", ([1, 2, 3], 7), 0),
    ("empty list", ([], 0), 0),
    ("all zeros", ([0, 0, 0], 0), 6),
    ("single element match", ([5], 5), 1),
]


if __name__ == "__main__":
    run_tests(subarray_sum, CASES)
