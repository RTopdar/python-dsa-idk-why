"""
27. Spiral Matrix  [Medium]  —  Loops / 2D arrays

Return all elements of an m x n matrix in clockwise spiral order.

Example:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]  ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]

Hint: keep top / bottom / left / right boundaries and shrink them.
"""

from _runner import run_tests


def spiral_order(matrix):
    # write your solution here
    pass


CASES = [
    ("example 1 (3x3)", ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ("3x4", ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ("single row", ([[1, 2, 3]],), [1, 2, 3]),
    ("single column", ([[1], [2], [3]],), [1, 2, 3]),
    ("1x1", ([[7]],), [7]),
    ("empty matrix", ([],), []),
    ("2x2", ([[1, 2], [3, 4]],), [1, 2, 4, 3]),
]


if __name__ == "__main__":
    run_tests(spiral_order, CASES)
