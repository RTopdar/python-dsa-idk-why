"""
48. Second Largest Distinct  [Easy]  —  Arrays / Loops

Return the second largest DISTINCT value in `nums`, or None if it doesn't
exist. Don't sort — do it in one loop with two variables.

Example:
    [3, 1, 4, 4, 2]  ->  3
    [5, 5, 5]        ->  None
"""

from _runner import run_tests


def second_largest(nums):
    # write your solution here
    pass


CASES = [
    ("example 1", ([3, 1, 4, 4, 2],), 3),
    ("all same", ([5, 5, 5],), None),
    ("empty", ([],), None),
    ("single", ([7],), None),
    ("negatives", ([-1, -5, -3],), -3),
    ("max at start", ([10, 2, 9],), 9),
    ("two values", ([1, 2],), 1),
]


if __name__ == "__main__":
    run_tests(second_largest, CASES)
