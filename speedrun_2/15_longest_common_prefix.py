"""
15. Longest Common Prefix  [Easy]  —  Strings / Loops

Return the longest prefix shared by every string in `strs`. Return "" if
there is none.

Example:
    ["flower", "flow", "flight"]  ->  "fl"
    ["dog", "racecar", "car"]     ->  ""
"""

from _runner import run_tests


def longest_common_prefix(strs):
    # write your solution here
    pass


CASES = [
    ("example 1", (["flower", "flow", "flight"],), "fl"),
    ("example 2", (["dog", "racecar", "car"],), ""),
    ("single string", (["alone"],), "alone"),
    ("empty list", ([],), ""),
    ("contains empty string", (["abc", ""],), ""),
    ("one is prefix of other", (["inter", "internet", "interval"],), "inter"),
    ("all identical", (["same", "same", "same"],), "same"),
]


if __name__ == "__main__":
    run_tests(longest_common_prefix, CASES)
