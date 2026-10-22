"""
28. Pascal's Triangle  [Easy]  —  Loops / Arrays

Return the first `num_rows` rows of Pascal's triangle. Each number is the
sum of the two numbers directly above it.

Example:
    num_rows = 5  ->  [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
"""

from _runner import run_tests


def generate_pascal(num_rows):
    # write your solution here
    pass


CASES = [
    ("example 1", (5,), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    ("one row", (1,), [[1]]),
    ("two rows", (2,), [[1], [1, 1]]),
    ("zero rows", (0,), []),
    ("row 7 check", (7,), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
                           [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]),
]


if __name__ == "__main__":
    run_tests(generate_pascal, CASES)
