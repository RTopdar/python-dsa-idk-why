"""
21. Top K Frequent Elements  [Medium]  —  Dictionaries / Sorting

Return the k most frequent values in `nums`, ordered from most frequent to
least frequent. (Test cases have no ties at the cut-off.)

Example:
    nums = [1, 1, 1, 2, 2, 3], k = 2  ->  [1, 2]

Try: dict counts + sorted(..., key=...), then try bucket sort for O(n).
"""

from _runner import run_tests


def top_k_frequent(nums, k):
    # write your solution here
    pass


CASES = [
    ("example 1", ([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    ("single element", ([1], 1), [1]),
    ("k equals unique count", ([4, 4, 5], 2), [4, 5]),
    ("negatives", ([-1, -1, -1, 2, 2, 3], 1), [-1]),
    ("most frequent at end", ([5, 6, 7, 7, 7, 7, 6], 2), [7, 6]),
    ("strings", (["py", "js", "py", "go", "py", "js"], 2), ["py", "js"]),
]


if __name__ == "__main__":
    run_tests(top_k_frequent, CASES)
