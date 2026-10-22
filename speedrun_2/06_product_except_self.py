"""
06. Product of Array Except Self  [Medium]  —  Arrays / Prefix

Return a list `answer` where answer[i] is the product of every element of
`nums` except nums[i]. Do NOT use division.

Example:
    [1, 2, 3, 4]  ->  [24, 12, 8, 6]

Goal: O(n) using a left-prefix pass and a right-suffix pass.
"""

from _runner import run_tests
import math

def product_except_self(nums):
    prefix = 1
    suffix = 1
    result=[]
    for i in range(len(nums)):
        prefix = math.prod(nums[0:i])
        suffix = math.prod(nums[i+1:len(nums)])
        result.append(prefix*suffix)
    return result


CASES = [
    ("example 1", ([1, 2, 3, 4],), [24, 12, 8, 6]),
    ("contains one zero", ([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    ("two zeros", ([0, 2, 0],), [0, 0, 0]),
    ("two elements", ([3, 5],), [5, 3]),
    ("all ones", ([1, 1, 1, 1],), [1, 1, 1, 1]),
    ("negatives", ([-2, -3, 4],), [-12, -8, 6]),
]


if __name__ == "__main__":
    run_tests(product_except_self, CASES)
