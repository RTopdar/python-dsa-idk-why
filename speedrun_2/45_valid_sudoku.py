"""
45. Valid Sudoku  [Medium]  —  Sets / Loops / 2D arrays

Check whether a 9x9 Sudoku board is VALID so far (not whether it's solvable).
Filled cells are "1".."9", empty cells are ".".
Rules: no repeated digit in any row, any column, or any 3x3 box.

Hint: one set per row, per column, per box. Box id = (r // 3, c // 3).
"""

from _runner import run_tests


def is_valid_sudoku(board):
    # write your solution here
    pass


CASES = [
    ("valid board", ([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],), True),
    ("repeat in column", ([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],), False),
    ("empty board", ([["."] * 9 for _ in range(9)],), True),
    ("repeat in row", ([["1", ".", ".", ".", ".", ".", ".", ".", "1"]] + [["."] * 9 for _ in range(8)],), False),
    ("repeat only in box", ([["1", ".", ".", ".", ".", ".", ".", ".", "."],
                             [".", "1", ".", ".", ".", ".", ".", ".", "."]] + [["."] * 9 for _ in range(7)],), False),
]


if __name__ == "__main__":
    run_tests(is_valid_sudoku, CASES)
