"""
19. Find All Duplicates  [Easy]  —  Sets / Loops

Return every value that appears more than once in `nums`, each listed once,
in the order its SECOND occurrence appears.

Example:
    [4, 3, 2, 7, 8, 2, 3, 1]  ->  [2, 3]
    [1, 1, 1, 2]              ->  [1]

Hint: two sets — `seen` and `added`.
"""

from _runner import run_tests


def find_duplicates(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([4, 3, 2, 7, 8, 2, 3, 1],), [2, 3]),
    ("triple shows once", ([1, 1, 1, 2],), [1]),
    ("no duplicates", ([1, 2, 3],), []),
    ("empty list", ([],), []),
    ("order of 2nd occurrence", ([5, 6, 6, 5],), [6, 5]),
    ("strings work too", (["a", "b", "a", "c", "b"],), ["a", "b"]),
]


if __name__ == "__main__":
    run_tests(find_duplicates, CASES)
