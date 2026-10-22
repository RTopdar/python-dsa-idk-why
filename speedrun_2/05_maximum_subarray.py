"""
05. Maximum Subarray  [Medium]  —  Arrays / Kadane

Find the contiguous subarray (at least one number) with the largest sum and
return that sum.

Example:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]  ->  6   ([4, -1, 2, 1])

Goal: O(n) with Kadane's algorithm.
"""

from _runner import run_tests


def max_subarray(nums):
    start = 0
    end = 0
    current_start=0
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i]>current_sum+ nums[i]:
            current_sum = nums[i]
            current_start = i
        else:
            current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
    return (max_sum, nums[start: end+1])

CASES = [
    ("example 1", ([-2, 1, -3, 4, -1, 2, 1, -5, 4],), (6, [4, -1, 2, 1])),
    ("single element", ([1],), (1, [1])),
    ("all positive", ([5, 4, -1, 7, 8],), (23, [5, 4, -1, 7, 8])),
    ("all negative", ([-3, -1, -2],), (-1, [-1])),
    ("single negative", ([-5],), (-5, [-5])),
    ("zeros and negatives", ([-1, 0, -2],), (0, [0])),
    ("best is whole array", ([2, -1, 2, -1, 2],), (4, [2, -1, 2, -1, 2])),
    ("negative prefix", ([-1, 3],), (3, [3])),
    ("restart after dip", ([1, 2, -10, 5],), (5, [5])),
    ("negative suffix dropped", ([5, -10],), (5, [5])),
    ("best in middle", ([-5, 4, -1, -1, 6, -10, 2],), (8, [4, -1, -1, 6])),
]


if __name__ == "__main__":
    run_tests(max_subarray, CASES)
