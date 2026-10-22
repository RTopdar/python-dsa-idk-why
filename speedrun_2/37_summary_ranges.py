"""
37. Summary Ranges  [Easy]  —  Arrays / Loops / Strings

`nums` is sorted with unique ints. Summarize it as ranges:
"a->b" for a run a..b, or "a" if the run has a single number.

Example:
    [0, 1, 2, 4, 5, 7]  ->  ["0->2", "4->5", "7"]
"""

from _runner import run_tests


def summary_ranges(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([0, 1, 2, 4, 5, 7],), ["0->2", "4->5", "7"]),
    ("example 2", ([0, 2, 3, 4, 6, 8, 9],), ["0", "2->4", "6", "8->9"]),
    ("empty", ([],), []),
    ("single", ([-1],), ["-1"]),
    ("one full run", ([3, 4, 5, 6],), ["3->6"]),
    ("all isolated", ([1, 3, 5],), ["1", "3", "5"]),
    ("negatives", ([-3, -2, -1, 1],), ["-3->-1", "1"]),
]


if __name__ == "__main__":
    run_tests(summary_ranges, CASES)
