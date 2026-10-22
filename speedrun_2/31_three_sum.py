"""
31. 3Sum  [Medium]  —  Arrays / Sorting / Two pointers

Return all UNIQUE triplets [a, b, c] from `nums` where a + b + c == 0.
Order of triplets and order inside a triplet don't matter (test normalizes).

Example:
    [-1, 0, 1, 2, -1, -4]  ->  [[-1, -1, 2], [-1, 0, 1]]

Goal: sort, then for each i use two pointers. Skip duplicates.
"""

from _runner import run_tests


def three_sum(nums):
    # write your solution here
    pass


def sort_triplets(triplets):
    return sorted(sorted(t) for t in triplets)


CASES = [
    ("example 1", ([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    ("no triplet", ([0, 1, 1],), []),
    ("all zeros", ([0, 0, 0, 0],), [[0, 0, 0]]),
    ("too short", ([1, -1],), []),
    ("empty list", ([],), []),
    ("many duplicates", ([-2, 0, 0, 2, 2],), [[-2, 0, 2]]),
    ("several answers", ([-4, -1, -1, 0, 1, 2],), [[-1, -1, 2], [-1, 0, 1]]),
]


if __name__ == "__main__":
    run_tests(three_sum, CASES, normalize=sort_triplets)
