"""
08. Merge Intervals  [Medium]  —  Arrays / Sorting / Loops

Given a list of [start, end] intervals, merge all overlapping intervals and
return them sorted by start. Touching intervals ([1,4] and [4,5]) merge.

Example:
    [[1,3], [2,6], [8,10], [15,18]]  ->  [[1,6], [8,10], [15,18]]
"""

from _runner import run_tests
import numpy as np


def merge_intervals(intervals):
    sorted_interval = sorted(intervals, key = lambda iv: iv[0])
    result = []
    for start,end in sorted_interval:
        if result and result[-1][1]>= start:
            result[-1][1]=max(end, result[-1][1])
        else:
            result.append([start,end])
    return result



CASES = [
    ("example 1", ([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    ("touching intervals", ([[1, 4], [4, 5]],), [[1, 5]]),
    ("unsorted input", ([[8, 10], [1, 3], [2, 6]],), [[1, 6], [8, 10]]),
    ("one contains another", ([[1, 10], [2, 3], [4, 5]],), [[1, 10]]),
    ("single interval", ([[5, 7]],), [[5, 7]]),
    ("empty list", ([],), []),
    ("no overlaps", ([[1, 2], [3, 4], [5, 6]],), [[1, 2], [3, 4], [5, 6]]),
]


if __name__ == "__main__":
    run_tests(merge_intervals, CASES)
    # merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
