"""
30. Valid Parentheses  [Easy]  —  Strings / Stack / Dictionaries

`s` contains only ()[]{} characters. Return True if every bracket is closed
by the same type, in the correct order.

Example:
    "()[]{}"  ->  True
    "(]"      ->  False
    "([)]"    ->  False
    "{[]}"    ->  True

Hint: list as a stack + dict {")": "(", "]": "[", "}": "{"}.
"""

from _runner import run_tests


def is_valid(s):
    # write your solution here
    pass


CASES = [
    ("example 1", ("()[]{}",), True),
    ("wrong type", ("(]",), False),
    ("wrong order", ("([)]",), False),
    ("nested", ("{[]}",), True),
    ("empty string", ("",), True),
    ("only opening", ("(((",), False),
    ("closing first", (")(",), False),
    ("deep nesting", ("({[({})]})",), True),
]


if __name__ == "__main__":
    run_tests(is_valid, CASES)
