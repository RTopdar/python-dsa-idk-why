"""
41. Rotate Image  [Medium]  —  Loops / 2D arrays

Rotate an n x n matrix 90 degrees clockwise and return it.

Example:
    [[1, 2, 3],         [[7, 4, 1],
     [4, 5, 6],   ->     [8, 5, 2],
     [7, 8, 9]]          [9, 6, 3]]

Bonus: in place = transpose, then reverse each row.
"""

from _runner import run_tests


def rotate_image(matrix):
    # write your solution here
    pass


CASES = [
    ("example 1 (3x3)", ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ("2x2", ([[1, 2], [3, 4]],), [[3, 1], [4, 2]]),
    ("1x1", ([[5]],), [[5]]),
    ("empty", ([],), []),
    ("4x4", ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
]


if __name__ == "__main__":
    run_tests(rotate_image, CASES)
