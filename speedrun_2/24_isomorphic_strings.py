"""
24. Isomorphic Strings  [Easy]  —  Dictionaries / Strings

Two strings are isomorphic if characters in `s` can be replaced to get `t`,
where each char maps to exactly one char and no two chars map to the same one.

Example:
    "egg", "add"      ->  True
    "foo", "bar"      ->  False
    "badc", "baba"    ->  False   (b->b and d->b clash)

Hint: two dicts (s->t and t->s).
"""

from _runner import run_tests


def is_isomorphic(s, t):
    # write your solution here
    pass


CASES = [
    ("example 1", ("egg", "add"), True),
    ("example 2", ("foo", "bar"), False),
    ("example 3", ("paper", "title"), True),
    ("two chars map to one", ("badc", "baba"), False),
    ("both empty", ("", ""), True),
    ("single chars", ("a", "z"), True),
    ("different lengths", ("ab", "abc"), False),
]


if __name__ == "__main__":
    run_tests(is_isomorphic, CASES)
