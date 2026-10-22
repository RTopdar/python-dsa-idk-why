"""
20. Group Anagrams  [Medium]  —  Dictionaries / Strings

Group words that are anagrams of each other. Return a list of groups.
Order of groups and order inside a group do NOT matter (test normalizes).

Example:
    ["eat","tea","tan","ate","nat","bat"]
        ->  [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Hint: dict key = "".join(sorted(word)) or a tuple of letter counts.
"""

from _runner import run_tests


def group_anagrams(words):
    # write your solution here
    pass


def sort_groups(groups):
    return sorted(sorted(g) for g in groups)


CASES = [
    ("example 1", (["eat", "tea", "tan", "ate", "nat", "bat"],),
     [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ("single empty string", ([""],), [[""]]),
    ("single word", (["a"],), [["a"]]),
    ("empty list", ([],), []),
    ("duplicate words", (["ab", "ba", "ab"],), [["ab", "ba", "ab"]]),
    ("no anagrams", (["abc", "def", "ghi"],), [["abc"], ["def"], ["ghi"]]),
]


if __name__ == "__main__":
    run_tests(group_anagrams, CASES, normalize=sort_groups)
