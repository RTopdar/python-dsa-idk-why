"""
03. Move Zeroes  [Easy]  —  Arrays / Two pointers

Move all 0s in `nums` to the end while keeping the order of non-zero
elements. Modify the list in place AND return it.

Example:
    [0, 1, 0, 3, 12]  ->  [1, 3, 12, 0, 0]

Goal: O(n) time, O(1) extra space (no new list).
"""

from _runner import run_tests


def move_zeroes(nums):
    write_index = 0
    for value in nums:
        if value!=0:
            nums[write_index]=value
            write_index+=1
    for i in range(write_index, len(nums)):
        nums[i]=0
    return nums


CASES = [
    ("example 1", ([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    ("single zero", ([0],), [0]),
    ("no zeroes", ([1, 2, 3],), [1, 2, 3]),
    ("all zeroes", ([0, 0, 0],), [0, 0, 0]),
    ("empty list", ([],), []),
    ("zeroes already at end", ([4, 5, 0, 0],), [4, 5, 0, 0]),
    ("negatives kept in order", ([0, -1, 0, -2, 3],), [-1, -2, 3, 0, 0]),
]


if __name__ == "__main__":
    run_tests(move_zeroes, CASES)
